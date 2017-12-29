# -*- coding: utf-8 -*-
from model.contact import Contact

    #тест1 - создаем контакт и заполняем основные поля
def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname="Alex", middlename="Serge", lastname="Pushkin", address="SPB", home="111", mobile="222", work="333", email="sasha@push.qq"))
    app.open_home_page()
    app.session.logout()

    #тест2 - создаем контакт с пустыми полями
def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname="", middlename="", lastname="", address="", home="", mobile="", work="", email=""))
    app.open_home_page()
    app.session.logout()
