#!python3
import sqlite3

__author__ = 'Preetam'


def main():
    db = sqlite3.connect("test.db")
    db.row_factory = sqlite3.Row    # Makes row below as object which is iterable
    db.execute('drop table if exists test')
    db.execute('create table test(name text, id int)')
    # Insert rows
    db.execute('insert into test (name, id) values (?,?)', ('test1', 1))
    db.execute('insert into test (name, id) values (?,?)', ('test2', 2))
    db.execute('insert into test (name, id) values (?,?)', ('test3', 3))
    db.execute('insert into test (name, id) values (?,?)', ('test4', 4))
    db.execute('insert into test (name, id) values (?,?)', ('test5', 5))
    db.commit()

    cursor = db.execute('select * from test order by id')
    for row in cursor:
        print(row)  # <sqlite3.Row object at 0x00000000009FF810>
        print(dict(row))    # {'id': 5, 'name': 'test5'}
        print(row['name'])  # test5

if __name__ == '__main__':
    main()