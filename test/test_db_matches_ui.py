from python_lessons.model.group import Group


def test_group_list(app, db):
    ui_list = app.group.get_group_list()

    # чистим пробелы в конце строки, т.к в БД они есть, а в UI не показываются
    # выкидываем поля header, footer, т.к. app.group.get_group_list() возвращает список только с id и name
    def clean(group):
        return Group(id=group.id, name=group.name.strip())

    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
