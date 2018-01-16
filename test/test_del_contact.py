# -*- coding: utf-8 -*-
from model.contact import Contact


# тест - удаляем контакт
def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Alex", middlename="Serge", lastname="Pushkin"))
    app.contact.delete_first_contact()
    app.open_home_page()