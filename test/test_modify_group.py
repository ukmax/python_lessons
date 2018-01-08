# -*- coding: utf-8 -*-
from model.group import Group


# тест - редактируем имя в группе
def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="new name"))


# тест - редактируем хедер в группе
def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="new header"))
