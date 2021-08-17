from sqlalchemy import create_engine, func, alias
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from ormCreate import Book


def tabquery(query, leng):
    print('|', end='')
    count = 0
    for a in query.column_descriptions:
        tab = a['name']
        if tab is None:
            tab = 'None'
        print(tab, end='')
        l = (leng - len(tab))
        print(' ' * l, end='')
        print('|', end='')
        count += 1
    print()
    print('-' * (leng * count + count + 1))

    for args in query:
        print('|', end='')
        for arg in args:
            tab = arg
            if tab is None:
                tab = 'None'
            print(tab, end='')
            l = (leng - len(str(tab)))
            print(' ' * l, end='')
            print('|', end='')
        print()
    print('-' * (leng * count + count + 1))


engine = create_engine("postgresql://postgres:0000@localhost/postgres", echo=False, echo_pool=False)
session = sessionmaker(bind=engine)
s = session()

#
pr =  s.query(Book.title, Book.price).order_by(Book.title)
tabquery(pr, 25)
au = s.query(Book.author, func.count(Book.amount).label('Count'), func.sum(Book.amount)).group_by(Book.author)

tabquery(au, 20)
a = s.query(Book.author, func.min(Book.price)).group_by(Book.author)
tabquery(a, 20)
