# -*- coding: utf-8 -*-
from model.group import Group

    #тест - редактируем имя в группе
def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="new", header="new", footer="new"))
    app.session.logout()