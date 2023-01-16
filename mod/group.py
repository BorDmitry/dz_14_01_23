from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from mod.database import Base


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer,  primary_key=True)
    group_name = Column(String(250), nullable=False)
    person = relationship('Person')

    def __repr__(self):
        return f"Группа  (ID: {self.id}, Имя: {self.group_name})"
    