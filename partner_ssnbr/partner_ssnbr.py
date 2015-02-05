# -*- coding: utf-8 -*-

from openerp import models, fields, api, _
import openerp.tools

class res_partner(models.Model):
    _inherit = 'res.partner'
    ss_number=fields.Char(string = 'ID-Number', required=False, size=30, help="Social Security Number")
