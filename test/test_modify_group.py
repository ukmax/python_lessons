# -*- coding: utf-8 -*-
import random
from python_lessons.model.group import Group


# тест - редактируем имя в группе
def test_modify_some_group_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    # выбираем случайную группу, которую будем редактировать
    group = random.choice(old_groups)
    # подготавливаем новые данные с id группы, которую будем редактировать
    new_data = Group(id=group.id, name="new name")
    # перезаписываем группу с использованием старого id
    app.group.modify_group_by_id(group.id, new_data)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups.remove(group)
    old_groups.append(new_data)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
