from datetime import datetime
from pony.orm import *
from python_lessons.model.group import Group
from python_lessons.model.contact import Contact
from pymysql.converters import encoders, decoders, convert_mysql_timestamp


class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        lastname = Optional(str, column='lastname')
        firstname = Optional(str, column='firstname')
        #маппинг на str, т.к. из БД почему-то получаем str, а не datetime
        deprecated = Optional(str, column='deprecated')

    def __init__(self, host, name, user, password):
        # при использовании Pony данные из БД могут преобразовываться для использования в объектах
        # conv - берем списки преобразователей типов из PyMySQL, а не по умолчанию из Pony
        conv = encoders
        conv.update(decoders)
        conv[datetime] = convert_mysql_timestamp
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=conv)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)

        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
        # выводим все записи из _table_ = 'group_list'
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), lastname=contact.lastname, firstname=contact.lastname)

        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
        # выводим записи из _table_ = 'addressbook', у которых пустое поле deprecated, хотя в БД там нули
        # нулевые даты из  БД преобразуются в None, т.к. используется преобразователь из PyMySQL
        # преобразователь определен в self.db.bind()
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))
