# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    #тест1 - создаем контакт и заполняем основные поля
def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Alex", middlename="Serge", lastname="Pushkin", address="SPB", home="111", mobile="222", work="333", email="sasha@push.qq"))
    app.open_home_page()
    app.logout()

    #тест2 - создаем контакт с пустыми полями
def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="", middlename="", lastname="", address="", home="", mobile="", work="", email=""))
    app.open_home_page()
    app.logout()
