from python_lessons.model.contact import Contact
import re
from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_contact(self, contact, add_to_group=None):
        wd = self.app.wd
        self.app.open_home_page()
        # добавление нового контакта
        wd.find_element_by_link_text("add new").click()
        # заполнение основных полей нового контакта
        self.fill_contact_form(contact)
        if add_to_group is not None:
            select = Select(wd.find_element_by_css_selector("select[name='new_group']"))
            select.select_by_value(add_to_group.id)
        wd.find_element_by_name("submit").click()
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_css_selector('input[value="Delete"]').click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_css_selector('input[value="Delete"]').click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def modify_contact_by_index(self, new_contact_data, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # нажимаем кнопку редактирования
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # заполнение основных полей нового контакта
        self.fill_contact_form(new_contact_data)
        # нажимаем кнопку update
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.contact_cache = None

    def modify_contact_by_id(self, new_contact_data, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        # нажимаем кнопку редактирования
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()
        # заполнение основных полей нового контакта
        self.fill_contact_form(new_contact_data)
        # нажимаем кнопку update
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("email", contact.email)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            rows = wd.find_elements_by_name("entry")
            print(rows)
            for element in rows:
                cells = element.find_elements_by_tag_name("td")
                lastname_text = cells[1].text
                firstname_text = cells[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                address = cells[3].text
                self.contact_cache.append(Contact(id=id, lastname=lastname_text, firstname=firstname_text,
                                                  address=address, all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(id=id, lastname=lastname, firstname=firstname,
                       address=address, email=email, email2=email2, email3=email3,
                       home=home, mobile=mobile, work=work, phone2=phone2)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        # если не нашлась строка на view page, то присваиваем номеру пустую строку,
        # т.к. wd из формы edit прочитает пустые поля, как пустые строки
        home_search = re.search("H: (.*)", text)
        if home_search is None:
            home = ""
        else:
            home = home_search.group(1)

        mobile_search = re.search("M: (.*)", text)
        if mobile_search is None:
            mobile = ""
        else:
            mobile = mobile_search.group(1)

        work_search = re.search("W: (.*)", text)
        if work_search is None:
            work = ""
        else:
            work = work_search.group(1)

        phone2_search = re.search("P: (.*)", text)
        if phone2_search is None:
            phone2 = ""
        else:
            phone2 = phone2_search.group(1)

        return Contact(home=home, mobile=mobile, work=work, phone2=phone2)
