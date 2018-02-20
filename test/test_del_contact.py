# -*- coding: utf-8 -*-
from model.contact import Contact
import random


# тест - удаляем контакт
def test_del_some_contact(app, db, check_ui):
    app.open_home_page()
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="Alex", middlename="Serge", lastname="Pushkin"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        sorted_new_db = sorted(new_contacts, key=Contact.id_or_max)
        sorted_new_ui = sorted(app.contact.get_contact_list, key=Contact.id_or_max)
        print("\nsorted_new_db " + str(sorted_new_db))
        print("\nsorted_new_ui " + str(sorted_new_ui))
        assert sorted_new_db == sorted_new_ui
    app.open_home_page()
