# -*- coding: utf-8 -*-
from python_lessons.fixture.group import *


def test_add_group(app, db, json_groups):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    sorted_old = sorted(old_groups, key=Group.id_or_max)
    sorted_new = sorted(new_groups, key=Group.id_or_max)
    print("\nsorted_old " + str(sorted_old))
    print("\nsorted_new " + str(sorted_new))
    assert sorted_old == sorted_new
