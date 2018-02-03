# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")]+[
    Group(name=random_string("name", 10), header=random_string("header", 10), footer=random_string("footer", 10))
    for i in range(3)
]


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