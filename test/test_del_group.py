# -*- coding: utf-8 -*-
from model.group import Group


# тест - удаление группы
def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.delete_first_group()


