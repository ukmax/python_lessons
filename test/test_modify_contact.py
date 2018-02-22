# -*- coding: utf-8 -*-
from python_lessons.model.contact import Contact
import random


# тест - редактируем имя в контакте
def test_modify_some_contact_firstname(app, db):
    # если нет ни одного контакта - создаем новый
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(lastname="L0", firstname="F0", address="SPB", email="some_email",
                                           home="111", mobile="222", work="333", phone2="444"))
    old_contacts = db.get_contact_list()
    # выбираем случайный контакт, который будем редактировать
    contact = random.choice(old_contacts)
    # запоминаем какой id был у контакта, который будем изменять и передаем его в контакт, которым будем перезаписывать
    new_data = Contact(id=contact.id, firstname="new_name")
    app.contact.modify_contact_by_id(new_data, contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    # перезаписываем из кода
    old_contacts.remove(contact)
    old_contacts.append(new_data)
    # old_contacts - изменили через код
    # new_contacts - изменили через тестируемую систему
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    app.open_home_page()
