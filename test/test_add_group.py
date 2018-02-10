# -*- coding: utf-8 -*-
from python_lessons.model.group import Group


def test_add_group(app, json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    sorted_old = sorted(old_groups, key=Group.id_or_max)
    sorted_new = sorted(new_groups, key=Group.id_or_max)
    print("\nsorted_old " + str(sorted_old))
    print("\nsorted_new " + str(sorted_new))
    assert sorted_old == sorted_new
