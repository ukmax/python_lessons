# -*- coding: utf-8 -*-
from model.contact import Contact


# тест1 - создаем контакт и заполняем основные поля
def test_add_contact(app):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    cont = Contact(lastname="L0", firstname="F0", address="SPB", email="some_email",
                   home="111", mobile="222", work="333", phone2="444")
    app.contact.create_contact(cont)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()

    old_contacts.append(cont)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    app.open_home_page()


# # # тест2 - создаем контакт с пустыми полями
# def test_add_empty_contact(app):
#     app.open_home_page()
#     old_contacts = app.contact.get_contact_list()
#     cont = Contact(lastname="", firstname="", address="", email="",
#                    home="", mobile="", work="", phone2="")
#     app.contact.create_contact(cont)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == app.contact.count()
#     old_contacts.append(cont)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
#     app.open_home_page()
