from faker import Faker

from mod.database import create_db, Session
from mod.person import Person
from mod.author import Author
from mod.group import Group


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):

    authors_names = ['А.С. Пушкин', 'М.Ю. Лермонтов', 'Ф.М. Достоевский', 'И. Шукшин', 'А. и Б. Стругацкие', 'Д. Чейз',
                       'А. Дюма', 'А. Конан Дойл', 'И. Ильф и Е. Петров', 'Л.Н. Толстой', 'Г. Уэльс', 'И.А. Гончаров']

    group1 = Group(group_name="читатели постоянные")
    group2 = Group(group_name="новые читатели")
    session.add(group1)
    session.add(group2)

    for key, it in enumerate(authors_names):
        author = Author(author_title=it)
        author.groups.append(group1)
        if key % 2 == 0:
            author.groups.append(group2)
        session.add(author)

    faker = Faker('ru_RU')
    group_list = [group1, group2]
    session.commit()

    for _ in range(30):
        full_name = faker.name().split()
        age = faker.random.randint(10, 70)
        group = faker.random.choice(group_list)
        person = Person(full_name, age, group.id)
        session.add(person)

    session.commit()
    session.close()
