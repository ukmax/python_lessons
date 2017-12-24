# -*- coding: utf-8 -*-
import unittest
from group import Group
from application import Application


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    #тест1 - создание группы
    def test_add_group(self):
        success = True
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="my_group", header="headertext", footer="footertext"))
        self.app.logout(success)

    # тест2 - создание пустой группы
    def test_add_empty_group(self):
        success = True
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.logout(success)

    def tearDown(self):
        self.app.destroy()
