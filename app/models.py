from flask import url_for
from flask_mongoengine import Document
from mongoengine import fields as fl
from werkzeug.security import generate_password_hash, check_password_hash


class User(Document):
    username = fl.StringField(max_length=20, required=True)
    password_hash = fl.StringField()
    refresh_token = fl.StringField()

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Contact(Document):
    full_name = fl.StringField(required=True, max_length=60)
    phone = fl.StringField(max_length=16)
    email = fl.StringField(max_length=30)

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
