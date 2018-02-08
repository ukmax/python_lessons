# -*- coding: utf-8 -*-
from python_lessons.model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number(maxlen):
    symbols = string.digits + "-" + "(" + ")"
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(lastname="", firstname="", address="", email="", home="", mobile="", work="", phone2="")]\
           + [Contact(lastname=random_string("lastname", 10), firstname=random_string("firstname", 10),
                      address=random_string("address", 10), email=random_string("email", 10),
                      home=random_number(10), mobile=random_number(10), work=random_number(10),
                      phone2=random_number(10))
              for i in range(3)]


@pytest.mark.parametrize("cont", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, cont):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(cont)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(cont)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    app.open_home_page()
