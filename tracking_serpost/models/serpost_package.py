import serpost
from odoo import api, fields, models


def _hash_record(date, message):
    return "{}-{}".format(date, message.lower())


class SerpostPackage(models.Model):

    _name = "serpost.package"
    _rec_name = "tracking_number"

    tracking_number = fields.Char("Tracking number", required=True)

    record_ids = fields.One2many("serpost.package.record", "package_id", readonly=True)
    records_quantity = fields.Integer(
        "Records quantity", compute="_compute_records_quantity"
    )

    @api.model
    def create(self, values):
        package = super().create(values)
        if self.env.context.get("fetch_after_create", False):
            package.fetch_data()
        return package

    @api.depends("record_ids")
    def _compute_records_quantity(self):
        for package in self:
            package.records_quantity = self.env["serpost.package.record"].search_count(
                [("package_id", "=", package.id)]
            )

    @api.multi
    def fetch_data(self):
        for package in self:
            data = serpost.query_tracking_code(package.tracking_number)
            hashes = package.record_ids.mapped(lambda x: x.hash)
            to_insert = [
                {
                    "date": fields.Datetime.to_string(item["date"]),
                    "message": item["message"],
                }
                for item in data
                if _hash_record(
                    fields.Datetime.to_string(item["date"]), item["message"]
                )
                not in hashes
            ]
            package.write({"record_ids": [(0, False, x) for x in to_insert]})


class SerpostPackageRecord(models.Model):

    _name = "serpost.package.record"
    _order = "date desc"

    package_id = fields.Many2one(
        "serpost.package", "Package", required=True, ondelete="cascade"
    )

    date = fields.Datetime("Date", required=True)
    message = fields.Char("Message", required=True, default="")
    hash = fields.Char(compute="_compute_hash")
    # Used to avoid insert duplicated records when fetch data many times

    @api.depends("date", "message")
    def _compute_hash(self):
        for record in self:
            record.hash = _hash_record(record.date, record.message)
