from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:0000@localhost/postgres", echo=False)

Base = declarative_base()
session = sessionmaker(bind=engine)
s = session()


class Book(Base):
    __tablename__ = 'Book'

    book_id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    author = Column(String(250), nullable=False)
    price = Column(DECIMAL, nullable=False)
    amount = Column(Integer, nullable=False)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    s.add_all([Book(title="Мастер и Маргарита", author="Булгаков М.А.", price=670.99, amount=3),
               Book(title="Белая гвардия", author="Булгаков М.А.", price=540.50, amount=5),
               Book(title="Идиот", author="Достоевский Ф.М.", price=460.00, amount=10),
               Book(title="Братья Карамазовы", author="Достоевский Ф.М.", price=799.01, amount=3),
               Book(title="Игрок", author="Достоевский Ф.М.", price=480.50, amount=10),
               Book(title="Стихотворения и поэмы", author="Есенин С.А.", price=650.00, amount=15)
               ])
    s.commit()
