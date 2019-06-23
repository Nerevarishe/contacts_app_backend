from flask_mongoengine import Document
from mongoengine import fields as fl


class Contact(Document):
    full_name = fl.StringField(required=True)
    phone = fl.StringField()
    email = fl.StringField()
