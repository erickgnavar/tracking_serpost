from odoo import fields, models


class PurchaseOrder(models.Model):

    _inherit = "purchase.order"

    serpost_package_id = fields.Many2one("serpost.package", "Serpost package")
    serpost_record_ids = fields.One2many(
        "serpost.package.record", related="serpost_package_id.record_ids", readonly=True
    )
