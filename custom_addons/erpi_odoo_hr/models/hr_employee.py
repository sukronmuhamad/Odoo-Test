# ~/odoo_dev/custom_addons/erpi_odoo_hr/models/hr_employee.py

from odoo import fields, models

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    bpjs_kesehatan_no = fields.Char(string="BPJS Kesehatan No.")
    bpjs_ketenagakerjaan_no = fields.Char(string="BPJS Ketenagakerjaan No.")
    
    blood_group = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    ], string='Blood Group')
    
    rhesus = fields.Selection([
        ('positive', 'Positive (+)'),
        ('negative', 'Negative (-)'),
    ], string='Rhesus')
    
    medical_record_no = fields.Char(string="Medical Record No.")