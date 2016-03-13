from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

pizza_toppings_association = Table('pizza_toppings_association', Base.metadata,
    Column('pizza_id', Integer, ForeignKey('pizza.id')),
    Column('topping_id', Integer, ForeignKey('topping.id'))
)

class Pizza(Base):
    __tablename__ = "pizza"
    id = Column(Integer, priamary_key=True)
    name = Column(String, nullable=False)
    toppings = relationship("Topping", secondary="pizza_toppings_association",
                            backref="pizzas")

class Topping(Base):
    __tablename__ = "topping"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


peppers = Topping(name="Peppers")
garlic = Topping(name="Garlic")
chilli = Topping(name="Chilli")

spicy_pepper = Pizza(name="Spicy Pepper")
spicy_pepper.toppings = [peppers, chilli]

vampire_weekend = Pizza(name="Vampire Weekend")
vampire_weekend.toppings = [garlic, chilli]
