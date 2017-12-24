# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False},
                            firefox_binary="C:/Program Files/Mozilla Firefox ESR/firefox.exe")
        self.wd.implicitly_wait(60)

    #тест1 - создание группы
    def test_add_group(self):
        success = True
        self.login(username="admin", password="secret")
        self.create_group(Group(name="my_group", header="headertext", footer="footertext"))
        self.logout(success)

    # тест2 - создание пустой группы
    def test_add_empty_group(self):
        success = True
        self.login(username="admin", password="secret")
        self.create_group(Group(name="", header="", footer=""))
        self.logout(success)

    def create_group(self, group):
        wd = self.wd
        #открываем страницу со списком групп
        self.open_groups_page()
        # создание новой группы
        wd.find_element_by_name("new").click()
        # заполняем поля формы
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        #подтверждаем создание группы
        wd.find_element_by_name("submit").click()
        #возвращаемся к списку групп
        self.return_to_groups_page()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def logout(self, success):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()
        self.assertTrue(success)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
