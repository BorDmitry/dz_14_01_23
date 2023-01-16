from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from mod.database import Base

association_table = Table('association', Base.metadata, Column('author_id', Integer, ForeignKey('authors.id')),
                          Column('group_id', Integer, ForeignKey('groups.id')))


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    author_title = Column(String(250), nullable=False)
    groups = relationship("Group", secondary=association_table, backref='group_author')

    def __repr__(self):
        return f"Автор (ID: {self.id}, ФИО: {self.author_title})"
