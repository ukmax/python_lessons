# -*- coding: utf-8 -*-
from model.contact import Contact


# тест - редактируем имя в контакте
def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="F0", lastname="L0"))
    old_contacts = app.contact.get_contact_list()
    #у заменяемого контакта сохраняем его id
    cont = Contact(firstname="new_name", id=old_contacts[0].id)
    app.contact.modify_first_contact(cont)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = Contact(firstname="L0 new_name")
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    app.open_home_page()


# # тест - редактируем номер телефона в контакте
# def test_modify_contact_mobile(app):
#     if app.contact.count() == 0:
#         app.contact.create_contact(Contact(firstname="Alex", middlename="Serge", lastname="Pushkin"))
#     app.contact.modify_first_contact(Contact(mobile="new_mobile"))
#     app.open_home_page()