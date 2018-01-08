# -*- coding: utf-8 -*-
from model.group import Group


# тест1 - создание группы
def test_add_group(app):
    app.group.create(Group(name="my_group", header="headertext", footer="footertext"))


# тест2 - создание пустой группы
def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))


