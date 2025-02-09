from odoo import models, fields, api
from datetime import datetime, timedelta


class ResPartnerCustomizations(models.Model):
    _inherit = "res.partner"

    birth_date = fields.Date(
        string="Birth Date"
    )

    @api.model
    def send_birthday_emails(self):
        today = datetime.today().date()
        three_days_later = today + timedelta(days=3)
        contacts = self.search([("birth_date", "!=", False)])
        for contact in contacts:
            if contact.birth_date and contact.birth_date.replace(year=today.year) == three_days_later:
                template = self.env.ref('contacts_customization.email_template_birthday_congrats')
                if template:
                    template.send_mail(contact.id, force_send=True)
