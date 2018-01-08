

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        # открываем страницу со списком групп
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
        # подтверждаем создание группы
        wd.find_element_by_name("submit").click()
        # возвращаемся к списку групп
        self.return_to_groups_page()

    def modify_first_group(self, edit_group):
        wd = self.app.wd
        # открываем страницу со списком групп
        self.open_groups_page()
        #выбираем первую группу
        wd.find_element_by_name("selected[]").click()
        # нажимаем кнопку Edit
        wd.find_element_by_name("edit").click()
        # заполняем поля формы новыми значениями
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(edit_group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(edit_group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(edit_group.footer)
        # подтверждаем изменение группы
        wd.find_element_by_name("update").click()
        # возвращаемся к списку групп
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        wd = self.app.wd
        # открываем страницу со списком групп
        self.open_groups_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
