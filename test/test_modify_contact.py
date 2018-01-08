# -*- coding: utf-8 -*-
from model.contact import Contact

    #тест - редактируем имя в контакте
def test_modify_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="new_firstname"))
    app.open_home_page()
    app.session.logout()

def test_modify_contact_mobile(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(mobile="new_mobile"))
    app.open_home_page()
    app.session.logout()