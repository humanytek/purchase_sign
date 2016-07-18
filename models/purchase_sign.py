from openerp import api, fields, models


class PurchaseSign(models.Model):
    _inherit = "purchase.order"

    is_signed = fields.Boolean()
