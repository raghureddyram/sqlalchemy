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
    starting_price = Column(Float(scale=2), nullable=False, default=1.00)
    owner_id = Column(Integer, ForeignKey('user.id'), nullable=False) #Item belons to user, hence owner_id foreign key

    bidders = relationship("User", secondary="bid",
                            backref="bidding_item")## item has many bidders through bid.



class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

    owned_items = relationship("Item", backref="owner") ##user has many (owns) items
    bidded_items = relationship("Item", secondary="bid", backref="bidder")##user(or a bidder) has many bidded_items through bid




class Bid(Base):
    __tablename__ = "bid"

    id = Column(Integer, primary_key=True)
    bidder_id = Column(Integer, ForeignKey('user.id'), nullable=False) #Bid belongs to user
    item_id = Column(Integer, ForeignKey('item.id'), nullable=False) #Bid belongs to an item
    price = Column(Float(scale=2), nullable=False, default=0.50)

Base.metadata.create_all(engine)

raghu = User(username="raghureddyram", password="hellohello")
steven = User(username="steven", password="smarty")
jason = User(username="jason", password="doubledutch")
session.add_all([raghu, steven, jason])
session.commit()

keyring = Item(name="keyring", description="place to hold keys", owner_id=raghu.id)
baseball = Item(name="baseball", owner_id=steven.id)
toothpaste = Item(name="toothpaste", owner_id=jason.id)

session.add_all([keyring, baseball, toothpaste])
session.commit()





# session.add(keyring)
# session.commit()
