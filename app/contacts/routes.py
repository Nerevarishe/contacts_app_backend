from flask import jsonify, request, abort
from app.contacts import bp
from app.models import Contact


# CORS???
@bp.route('/', methods=['OPTIONS'])
def index():
    return '', 200


# Create new Contact
@bp.route('/contacts', methods=['POST'])
def create_new_contact():
    """ Return JSON with new created Contact """
    if not request.json or not request.json.get('fullName'):
        abort(400)
    contact = Contact(
        full_name=request.json.get('fullName'),
        phone=request.json.get('phone') or '',
        email=request.json.get('email') or ''
    )
    contact.save()

    return jsonify(contact.to_json()), 201


# Update existing contact by ID
@bp.route('/contacts/<contact_id>', methods=['PUT'])
def update_contact(contact_id):
    """ Return JSON with updated Contact """
    if not request.json['fullName']:
        abort(400)
    contact = Contact.objects.get_or_404(id=contact_id)
    contact.full_name = request.json.get('fullName')
    contact.phone = request.json.get('phone')
    contact.email = request.json.get('email')
    contact.save()
    return jsonify(contact.to_json())


# Delete existing contact by ID
@bp.route('/contacts/<contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    """ Return True if contact deleted """

    contact = Contact.objects.get_or_404(id=contact_id)
    contact.delete()
    return jsonify({'result': True})


# Get one contact by ID
@bp.route('/contacts/<contact_id>', methods=['GET'])
def get_one_contact(contact_id):
    """ Return JSON with one contact by ID """

    contact = Contact.objects.get_or_404(id=contact_id)

    return jsonify({'contact': contact.to_json()})


# Get all contacts
@bp.route('/contacts', methods=['GET', 'OPTIONS'])
def get_all_contacts():
    """ Return json with all contacts from DB"""
    contacts = Contact.objects.all()
    contacts_json = []
    for contact in contacts:
        contacts_json.append(contact.to_json(add_uri=True))
    return jsonify(contacts_json)

