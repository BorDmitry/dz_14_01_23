import os

from sqlalchemy import and_, func, text

from mod.database import DATABASE_NAME, Session
import create_database as db_creator

from mod.author import Author, association_table
from mod.person import Person
from mod.group import Group

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session = Session()

    for it in session.query(Author):
        print(it)
    print("*" * 60)

    for it in session.query(Author).filter(Author.id <= 6, Author.author_title.like('%у%')):
        print(it)
    print("*" * 60)

    for it in session.query(Author).filter(and_(Author.id >= 7, Author.author_title.like('И%'))):
        print(it)
    print("*" * 60)

    for it, gr in session.query(Author.author_title, Group.group_name).filter(and_(association_table.c.author_id ==
    Author.id, association_table.c.group_id == Group.id, Group.group_name == 'читатели постоянные')):
        print(it, gr)
    print("*" * 60)

    print(session.query(Person).filter(Person.age.between(18, 35)).all())
    print("*" * 60)

    for it in session.query(Person).join(Group).filter(Group.group_name == 'новые читатели'):
        print(it)
    print("*" * 60)

    for it in session.query(func.count(Person.surname), Group.group_name).join(Group).group_by(Group.group_name):
        print(it)
    print("*" * 60)

    k = session.query(Author).get(6)
    k.author_title = "Р.Л. Стивенсон"
    session.add(k)
    session.commit()

    for it in session.query(Author):
        print(it.author_title)
    print("*" * 60)

    session.add(Author(author_title="Марк Твен"))
    session.commit()

    for it in session.query(Author):
        print(it.id, it.author_title)
    print("*" * 60)

    for it in session.query(Person).filter(text("surname like 'С%'")).order_by(text("name, id desc")):
        print(it)
    print("*" * 60)

    i = session.query(Author).filter(Author.author_title == "Марк Твен").first()
    print(i)
    session.delete(i)
    session.commit()

    for it in session.query(Author):
        print(it.author_title)
    print("*" * 60)

