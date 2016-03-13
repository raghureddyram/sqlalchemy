from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey



engine = create_engine('postgresql://vagrant:vagrant@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)

    owner_id = Column(Integer, ForeignKey('user.id'), nullable=False)

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    items = relationship("Item", backref="owner") ##if uselist=False ommitted then will be one-to-many

class Bid(Base):
    __tablename__ = "bid"

    id = Column(Integer, primary_key=True)
    price = Column(Float(scale=2), nullable=False)

Base.metadata.create_all(engine)

raghu = User(username="raghureddyram", password="hellohello")
steven = User(username="steven", password="smarty")
# session.add_all([raghu, steven])
# session.commit()
keyring = Item(name="keyring", description="place to hold keys", owner_id=raghu.id)

# session.add(keyring)
# session.commit()
