# -*- coding: utf-8 -*-
from model.group import Group


# тест - редактируем имя в группе
def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(name="new name"))


# тест - редактируем хедер в группе
def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="test"))
    app.group.modify_first_group(Group(header="new header"))
