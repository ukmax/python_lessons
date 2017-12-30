# -*- coding: utf-8 -*-
from model.group import Group

    #тест - редактируем имя в контакте
def test_edit_first_contact_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="new", header="new", footer="new"))
    app.session.logout()