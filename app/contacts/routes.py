from flask import jsonify, request
from app.contacts import bp
from app.models import Contact


# Create new Contact
@bp.route('/contacts', methods=['POST'])
def create_new_contact():

    """ Return JSON with new created Contact """

    contact = Contact(
        full_name=request.json.get('full_name'),
        phone=request.json.get('phone'),
        email=request.json.get('email')
    )
    contact.save()

    return jsonify({'contact': {
        'id': str(contact.id),
        'full_name': str(contact.full_name),
        'phone': str(contact.phone),
        'email': str(contact.email)
    }}), 201


# Update existing contact by ID
@bp.route('/contacts/<contact_id>', methods=['PUT'])
def update_contact(contact_id):

    """ Return JSON with updated Contact """

    pass


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

    return jsonify({'contact': {
        'id': str(contact.id),
        'full_name': str(contact.full_name),
        'phone': str(contact.phone),
        'email': str(contact.email)
    }})


# Get all contacts
@bp.route('/contacts', methods=['GET'])
def get_all_contacts():

    """ Return json with all contacts from DB"""

    contacts = Contact.objects.all()
    contacts_json = []
    for contact in contacts:
        contacts_json.append({
            'id': str(contact.id),
            'full_name': str(contact.full_name),
            'phone': str(contact.phone),
            'email': str(contact.email)
        })
    return jsonify({'contacts': contacts_json})
