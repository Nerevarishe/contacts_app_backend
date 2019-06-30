from flask import url_for
from flask_mongoengine import Document
from mongoengine import fields as fl


class Contact(Document):
    full_name = fl.StringField(required=True)
    phone = fl.StringField()
    email = fl.StringField()

    def to_json(self, add_full_uri=False, add_uri=False):
        """ Return contact in form of dic, for use with flask jsonify function """
        contact = {
            'id': str(self.id),
            'fullName': str(self.full_name),
            'phone': str(self.phone),
            'email': str(self.email),
        }

        if add_full_uri:
            contact.update({'uri': url_for('contacts.get_one_contact', contact_id=self.id, _external=True)})

        if add_uri:
            contact.update({'uri': url_for('contacts.get_one_contact', contact_id=self.id)})

        return contact
