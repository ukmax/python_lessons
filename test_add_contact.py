# -*- coding: utf-8 -*-
import unittest
from contact import Contact
from application import Application


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    #тест1 - создаем контакт и заполняем основные поля
    def test_add_contact(self):
        success = True
        self.app.login(username="admin", password="secret")
        self.app.create_contact(Contact(firstname="Alex", middlename="Serge", lastname="Pushkin", address="SPB", home="111", mobile="222", work="333", email="sasha@push.qq"))
        self.app.open_home_page()
        self.app.logout(success)

    #тест2 - создаем контакт с пустыми полями
    def test_add_empty_contact(self):
        success = True
        self.app.login(username="admin", password="secret")
        self.app.create_contact(Contact(firstname="", middlename="", lastname="", address="", home="", mobile="", work="", email=""))
        self.app.open_home_page()
        self.app.logout(success)

    def tearDown(self):
        self.app.destroy()