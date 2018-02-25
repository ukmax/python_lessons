# -*- coding: utf-8 -*-
from python_lessons.model.contact import Contact
from python_lessons.model.group import Group
from python_lessons.fixture.orm import ORMFixture
import random


def test_add_contact_to_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group_list = db.get_group_list()
    rand_group = random.choice(group_list)

    def generate_new_contact_id():
        id_list = db.get_all_contact_id_list()
        new_id = max(id_list) + 1
        return str(new_id)

    new_contact = Contact(id=generate_new_contact_id(), lastname="lll8", firstname="fff")
    app.open_home_page()
    app.contact.create_contact(new_contact, add_to_group=rand_group)
    orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    contacts_in_group = orm.get_contacts_in_group(rand_group)
    assert new_contact in contacts_in_group
