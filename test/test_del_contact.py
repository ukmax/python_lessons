# -*- coding: utf-8 -*-
from model.contact import Contact

    #тест - удаляем контакт
def test_del_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.open_home_page()
    app.session.logout()