#!python3

import sqlite3
__author__ = 'Preetam'


# Class database
class Database(object):

    # Constructor
    def __init__(self, **kwargs):
        self.filename = kwargs.get('filename', 'test.db')
        self.table = kwargs.get('table', 'test')

    # Iterable class
    def __iter__(self):
        cursor = self._db.execute('select * from {}'.format(self._table))
        for row in cursor:
            yield dict(row)

    # Insert table
    def insert(self, row):
        self._db.execute('insert into {} (name, id) values (?,?)'.format(self.table), (row['name'], row['id']))
        self._db.commit()

    # Update table
    def update(self, row):
        self._db.execute('update test set name = ? where id = ?', (row['name'], row['id']))
        self._db.commit()

    # Delete row
    def delete(self, key):
        self._db.execute('delete from {} where id = ?'.format(self._table), (key,))
        self._db.commit()

    # Retrieve for select query
    def retrieve(self, key):
        cursor = self._db.execute('select * from {} where id = ?'.format(self._table), (key,))
        return dict(cursor.fetchone())

    # Use properties of the class as accessor

    # filename
    @property
    def filename(self):
        return self._filename

    # Setter also connects the db
    @filename.setter
    def filename(self, f):
        self._db = sqlite3.connect(f)
        self._db.row_factory = sqlite3.Row
        self._filename = f

    @filename.deleter
    def filename(self):
        self._filename = 'test.db'

    # table
    @property
    def table(self):
        return self._table

    @table.setter
    def table(self, t):
        self._table= t

    # Delete defaults the table name to test
    @table.deleter
    def table(self):
        self.table = 'test'

def main():
    test_db = Database(filename='test.db', table='test')

    # Rest functions are as in crud_operations.py file
    for row in test_db: # Database acts as iterable
        print(row)

if __name__ == '__main__':
    main()