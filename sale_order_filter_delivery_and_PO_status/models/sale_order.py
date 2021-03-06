# -*- coding: utf-8 -*-


from odoo import api, fields, models


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    delivery_status_not_done = fields.Boolean(
        compute='_compute_boolean_delivery_status',
        search='_search_delivery_status',
        )

    purchase_status_open = fields.Boolean(
        compute='_compute_boolean_purchase_status',
        search='_search_purchase_status',
        )

    @api.multi
    def _compute_boolean_delivery_status(self):
        for order in self:
            if order.delivery_status != 'done':
                order.delivery_status_not_done = True

    @api.multi
    def _search_delivery_status(self, operator, value):
        recs = self.search([]).filtered(
            lambda x: x.delivery_status_not_done is True)
        if recs:
            return [('id', 'in', [x.id for x in recs])]

    @api.multi
    def _compute_boolean_purchase_status(self):
        for order in self:
            if order.purchase_status == 'open':
                order.purchase_status_open = True

    @api.multi
    def _search_purchase_status(self, operator, value):
        recs = self.search([]).filtered(
            lambda x: x.purchase_status_open is True)
        if recs:
            return [('id', 'in', [x.id for x in recs])]
