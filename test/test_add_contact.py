# -*- coding: utf-8 -*-
from python_lessons.model.contact import Contact


def test_add_contact(app, json_contacts):
    cont = json_contacts
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(cont)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(cont)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    app.open_home_page()
