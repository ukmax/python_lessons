# -*- coding: utf-8 -*-
from model.contact import Contact


# тест - удаляем контакт
def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Alex", middlename="Serge", lastname="Pushkin"))
    old_contacts = app.contact.get_contact_list()
    print(old_contacts)
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    print(new_contacts)
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    print(old_contacts)
    assert old_contacts == new_contacts
    app.open_home_page()
