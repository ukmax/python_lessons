import re
from random import randrange
from model.contact import Contact


# сравнение контактов на homepage и в db
def test_phones_on_db(app, db):
    app.open_home_page()
    if (len(db.get_contact_list())) == 0:
        app.contact.create_contact(Contact(lastname="LL", firstname="FF", address="aa", email="q@w.e", home="111"))
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list()
    sorted_contact_from_home_page = sorted(contact_from_home_page, key=Contact.id_or_max)
    sorted_contact_from_db = sorted(contact_from_db, key=Contact.id_or_max)
    assert sorted_contact_from_home_page == sorted_contact_from_db


# сравнение контактов на homepage и на editpage
def test_phones_on_home_page(app):
    app.open_home_page()
    contact_length = app.contact.count()
    if contact_length == 0:
        app.contact.create_contact(Contact(lastname="LL", firstname="FF", address="aa", email="q@w.e", home="111"))
    index = randrange(contact_length)
    print('\nindex= ' + str(index))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    # сравниваем склееный список телефонов с главной и список с формы редактирования, который сами почистили и склеили
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


# сравнение контактов на viewpage и на editpage
def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def merge_phones_like_on_home_page(contact):
    # берем все значения номеров из контакта
    step1 = [contact.home, contact.mobile, contact.work, contact.phone2]
    # выкидываем из прочитанных полей пустые значения
    step2 = filter(lambda x: x is not None, step1)
    # к оставшимся элементам применяем clear(), которая удаляет лишние символы, не отображающиеся в таблице)
    step3 = map(lambda x: clear(x), step2)
    # выкидываем пустые строки, которые могли возникнуть в результате очистки
    step4 = filter(lambda x: x != "", step3)
    # то, что осталось от фильтрации склеивается при помощи перевода строки
    phones_joined = "\n".join(step4)
    return phones_joined


def merge_emails_like_on_home_page(contact):
    # берем все значения номеров из контакта
    step1 = [contact.email, contact.email2, contact.email3]
    # выкидываем из прочитанных полей пустые значения
    step2 = filter(lambda x: x != "", step1)
    emails_joined = "\n".join(step2)
    return emails_joined


# чистим строку от "плохих" символов
def clear(s):
    return re.sub("[() -]", "", s)
