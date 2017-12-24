# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    #тест1 - создание группы
def test_add_group(app):
    success = True
    app.login(username="admin", password="secret")
    app.create_group(Group(name="my_group", header="headertext", footer="footertext"))
    app.logout(success)

    # тест2 - создание пустой группы
def test_add_empty_group(app):
    success = True
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout(success)

