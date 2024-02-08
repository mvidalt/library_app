from odoo import fields, models
from odoo.exceptions import ValidationError

class LibraryMember(models.Model):
    _name = "library.member"
    _description = "Library Member"

    card_number = fields.Char("Library Card Number", required=True)
    name = fields.Char("Full Name", required=True)
    address = fields.Text("Address")
    email = fields.Char("Email")


