# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


# тест - удаляем контакт
def test_del_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Alex", middlename="Serge", lastname="Pushkin"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    app.open_home_page()
