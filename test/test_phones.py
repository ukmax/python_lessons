import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def merge_phones_like_on_home_page(contact):
    # берем все значения номеров из контакта
    phones = [contact.home, contact.mobile, contact.work, contact.phone2]
    # выкидываем из прочитанных полей пустые значения
    phones2 = filter(lambda x: x is not None, phones)
    # к оставшимся элементам применяем clear(), которая удаляет лишние символы, не отображающиеся в таблице)
    phones3 = map(lambda x: clear(x), phones2)
    # выкидываем пустые строки, которые могли возникнуть в результате очистки
    phones4 = filter(lambda x: x != "", phones3)
    # то, что осталось от фильтрации склеивается при помощи перевода строки
    phones_joined = "\n".join(phones4)
    return phones_joined


# чистим строку от "плохих" символов
def clear(s):
    return re.sub("[() -]", "", s)


# def merge_phones_like_on_home_page(contact):
#     return "\n".join(filter(lambda x: x != "",
#                             map(lambda x: clear(x),
#                                 filter(lambda x: x is not None,
#                                        [contact.home, contact.work, contact.mobile, contact.phone2]))))
