from sqlalchemy import Column, ForeignKey, Integer, String

from mod.database import Base


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    surname = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    patronymic = Column(String(250), nullable=False)
    age = Column(Integer)
    group = Column(Integer, ForeignKey('groups.id'))

    def __init__(self, full_name, age, id_group):
        self.surname = full_name[0]
        self.name = full_name[1]
        self.patronymic = full_name[2]
        self.age = age
        self.group = id_group

    def __repr__(self):
        return f"Персона (Имя: {self.surname} {self.name} {self.patronymic}, Возраст {self.age}, ID группы:" \
               f"{self.group})"

