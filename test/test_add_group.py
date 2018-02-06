# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from data.add_group import testdata


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups)+1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    sorted_old = sorted(old_groups, key=Group.id_or_max)
    sorted_new = sorted(new_groups, key=Group.id_or_max)
    print("\nsorted_old "+str(sorted_old))
    print("\nsorted_new " + str(sorted_new))
    assert sorted_old == sorted_new