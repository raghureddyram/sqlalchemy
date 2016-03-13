from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey

#missing the create_engine statements and database


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    passport = relationship("Passport", uselist=False, backref="owner")

class Passport(Base):
    __tablename__ = 'passport'
    id = Column(Integer, primary_key=True)
    issue_date = Column(Date, nullable=False, default=datetime.utcnow)

    owner_id = Column(Integer, ForeginKey('person.id'), nullable=False)

beyonce = Person(name='Beyonce')
passport = Passport(owner_id=beyonce.id)
session.add_all([beyonce, passport])
session.commmit()


## adding only beyonce will only persist beyonce to db but keep passport in memory
# beyonce = Person(name="Beyonce Knowles")
# passport = Passport()
# beyonce.passport = passport
#
# session.add(beyonce)
# session.commit()
#
# print(beyonce.passport.issue_date)
# print(passport.owner.name)
