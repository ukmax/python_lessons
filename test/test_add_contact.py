# -*- coding: utf-8 -*-
from model.contact import Contact


# тест1 - создаем контакт и заполняем основные поля
def test_add_contact(app):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    #cont = Contact(firstname="F0", middlename="M0", lastname="L0", address="SPB", home="111", mobile="222", work="333", email="sasha@push.qq")
    cont = Contact(firstname="F0", lastname="L0")
    app.contact.create_contact(cont)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    #old_contacts.append(cont)
    old_contacts.append(Contact(firstname="L0 F0"))
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    app.open_home_page()


# # тест2 - создаем контакт с пустыми полями
# def test_add_empty_contact(app):
#     app.open_home_page()
#     app.contact.create_contact(Contact(firstname="", middlename="", lastname="", address="", home="", mobile="", work="", email=""))
#     app.open_home_page()
