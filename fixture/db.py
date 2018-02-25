import pymysql.cursors
import mysql.connector
from python_lessons.model.group import Group
from python_lessons.model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        #  self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit(True)

    def destroy(self):
        self.connection.close()

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                # в переменные присваиваем значения из кортежа, который соответствует строке
                (id, name, header, footer) = row
                # делаем приведение типов для id, т.к. в БД id это int, а из web читаем как str
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, lastname, firstname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                # в переменные присваиваем значения из кортежа, который соответствует строке
                (id, lastname, firstname) = row
                # делаем приведение типов для id, т.к. в БД id это int, а из web читаем как str
                list.append(Contact(id=str(id), lastname=lastname, firstname=firstname))
        finally:
            cursor.close()
        return list

    def get_all_contact_id_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id from addressbook")
            for row in cursor:
                # row - это tuple
                id = row[0]
                list.append(id)
        finally:
            cursor.close()
        return list
