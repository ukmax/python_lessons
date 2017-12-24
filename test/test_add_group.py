# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    #тест1 - создание группы
def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="my_group", header="headertext", footer="footertext"))
    app.session.logout()

    # тест2 - создание пустой группы
def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()

