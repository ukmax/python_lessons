# -*- coding: utf-8 -*-
from model.group import Group

    #тест - редактируем имя в группе
def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="new name"))
    app.session.logout()

def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(header="new header"))
    app.session.logout()