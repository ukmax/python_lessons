# -*- coding: utf-8 -*-
from model.contact import Contact

    #тест - редактируем имя в контакте
def test_modify_contact_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="new_name", middlename="new_name", lastname="new_name", address="new_name", home="new_name", mobile="new_name", work="", email="new_name"))
    app.open_home_page()
    app.session.logout()