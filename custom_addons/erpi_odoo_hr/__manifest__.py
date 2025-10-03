{
    'name': "ERPI Odoo HR Customization",
    'version': '16.0.1.0.0',
    'summary': 'Menambahkan data kustom BPJS dan Medis pada Karyawan.',
    'description': """
        Modul ini berfungsi untuk mendata data pegawai. Terdapat kolom-kolom yang
        berkaitan dengan data karyawan seperti: No BPJS Kesehatan, No BPJS Ketenagakerjaan,
        golongan darah, Rhesus darah, dan medical record.
    """,
    'author': "Your Name",
    'website': "Your Website",
    'category': 'Human Resources',
    'depends': ['hr', 'mail'],
    'data': [
        'views/hr_employee_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}