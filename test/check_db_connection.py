from python_lessons.fixture.orm import ORMFixture
from python_lessons.model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_contacts_in_group(Group(id='337'))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass  # db.destroy()
