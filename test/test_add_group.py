# -*- coding: utf-8 -*-
from model.group import Group

    #тест1 - создание группы
def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="my_group", header="headertext", footer="footertext"))
    app.session.logout()

    # тест2 - создание пустой группы
def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

