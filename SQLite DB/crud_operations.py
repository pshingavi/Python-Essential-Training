#!python3
import sqlite3

__author__ = 'Preetam'


# Display rows
def display_rows(db):
    cursor = db.execute('select * from test order by id')
    for row in cursor:
        print(dict(row))


# Insert
def insert(db, row):
    db.execute('insert into test (name, id) values(?,?)', (row['name'], row['id']))
    db.commit()


# Retrieve
def retrieve(db, id):
    cursor = db.execute('select * from test where id = ?',(id,))
    return cursor.fetchone()


# Update
def update(db, row):
    db.execute('update test set name = ? where id = ?',(row['name'], row['id']))
    db.commit()


# Delete
def delete(db, id):
    db.execute('delete from test where id = ?', (id,))
    db.commit()


# Main
def main():
    db = sqlite3.connect("test.db")
    db.row_factory = sqlite3.Row

    print("Creating data base table")
    db.execute('drop table if exists test')
    db.execute('create table test (name text, id int)')

    print('Insert rows')
    insert(db, dict(name="test1", id=1))
    insert(db, dict(name="test2", id=2))
    insert(db, dict(name="test3", id=3))
    insert(db, dict(name="test4", id=4))
    display_rows(db)

    print('Retrieve rows')
    print(dict(retrieve(db, 2))) # {'id': 2, 'name': 'test2'}

    print('Update rows')
    update(db, dict(name='updated_test2',id=2))
    display_rows(db)

    print('Delete rows')
    delete(db,2)
    display_rows(db)

if __name__ == '__main__':
    main()