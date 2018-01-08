# -*- coding: utf-8 -*-


# тест - удаляем контакт
def test_del_first_contact(app):
    app.contact.delete_first_contact()
    app.open_home_page()