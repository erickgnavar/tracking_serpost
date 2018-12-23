from odoo import fields, models


class SaleOrder(models.Model):

    _inherit = "sale.order"

    serpost_package_id = fields.Many2one("serpost.package", "Serpost package")
    serpost_record_ids = fields.One2many(
        "serpost.package.record", related="serpost_package_id.record_ids", readonly=True
    )
