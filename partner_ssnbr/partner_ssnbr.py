# -*- coding: utf-8 -*-

from openerp import models, fields, api, _
import openerp.tools
import re

class ssnbr(models.Model):
    _inherit = 'res.partner'
    ss_number=fields.Char(String = 'Social Security Number', required=True, size=10)
