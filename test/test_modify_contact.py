# -*- coding: utf-8 -*-
from model.contact import Contact


# тест - редактируем имя в контакте
def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="new_firstname"))
    app.open_home_page()


# тест - редактируем номер телефона в контакте
def test_modify_contact_mobile(app):
    app.contact.modify_first_contact(Contact(mobile="new_mobile"))
    app.open_home_page()