# -*- coding: utf-8 -*-
from model.contact import Contact


# тест1 - создаем контакт и заполняем основные поля
def test_add_contact(app):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    cont = Contact(firstname="F0", middlename="M0", lastname="L0", address="SPB", mobile="111222333", email="sasha@push.kin")
    app.contact.create_contact(cont)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(cont)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    app.open_home_page()


# # тест2 - создаем контакт с пустыми полями
def test_add_empty_contact(app):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    cont = Contact(firstname="", middlename="", lastname="", address="", mobile="")
    app.contact.create_contact(cont)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(cont)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    app.open_home_page()