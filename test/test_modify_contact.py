# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


# тест - редактируем имя в контакте
def test_modify_some_contact_firstname(app):
    # если нет ни одного контакта - создаем новый
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="F0", lastname="L0"))
    old_contacts = app.contact.get_contact_list()
    # выбираем случайную запись
    index = randrange(len(old_contacts))
    # запоминаем какой id был у контакта, который будем изменять и передаем его в контакт, которым будем перезаписывать
    cont = Contact(firstname="new_name", id=old_contacts[index].id)
    app.contact.modify_first_contact(cont, index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    # перезаписываем из кода
    old_contacts[index] = cont
    # old_contacts - изменили через код
    # new_contacts - изменили через тестируемую систему
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    app.open_home_page()


# # тест - редактируем номер телефона в контакте
# def test_modify_contact_mobile(app):
#     if app.contact.count() == 0:
#         app.contact.create_contact(Contact(firstname="F0", lastname="L0"))
#     old_contacts = app.contact.get_contact_list()
#     #у заменяемого контакта сохраняем его id
#     cont = Contact(mobile="new_mobile", id=old_contacts[0].id)
#     app.contact.modify_first_contact(cont)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#     old_contacts[0] = cont
#     assert sorted(new_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
#     app.open_home_page()