# -*- coding: utf-8 -*-
#from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application():
    def __init__(self, browser, base_url):
        if browser == "firefox":
            # self.wd = WebDriver(capabilities={"marionette": False}, firefox_binary="C:/Program Files/Mozilla Firefox ESR/firefox.exe")
            self.wd = webdriver.Firefox(capabilities={"marionette": False})
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)

        # self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def destroy(self):
        self.wd.quit()

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath("//div[@id='content']/form[2]/div[1]/input")) > 0):
            wd.get(self.base_url)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


