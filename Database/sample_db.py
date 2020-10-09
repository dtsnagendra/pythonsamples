

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(f'exception occured .. {e}')
    
    #conn.close()
    return conn

def create_table(conn):
    #CREATE TABLE IF NOT EXISTS <tablename> ( colname <datatype>, col2 <datatype>);

    table_query = """CREATE TABLE IF NOT EXISTS STUDENT (
        Id  integer PRIMARY KEY,
        Name text,
        Location text);"""

    try:
        c = conn.cursor()
        c.execute(table_query)
    except Error as e:
        print(e)

def insert_data(conn):
    sql_query = 'insert into student(Id, Name, Location) values(?,?,?)'
    vals = ('1004','Swetha','USA')
    c = conn.cursor()
    c.execute(sql_query,vals)
    conn.commit()

def select_data(conn):
    qu = 'select * from student'
    c = conn.cursor()
    c.execute(qu)
    records = c.fetchall()
    for re in records:
        print(re)

def update_data(conn):
    # update <tablename> set <colname> = <value> where <colname> = <value>
    # update student set Location = ?, Name = ? where Id =?
    country = input("Enter Country Name : ")
    name = input("Enter Name : ")
    qu = 'update student set Location = ?, Name=? where Id = ?'
    vals = (country,name,'1002')
    #vals = (name, sal, job)
    c = conn.cursor()
    c.execute(qu,vals)
    conn.commit()

def remove_data(conn):
    # update <tablename> set <colname> = <value> where <colname> = <value>
    # update student set Location = ?, Name = ? where Id =?
    #country = input("Enter Country Name : ")
    #name = input("Enter Name : ")
    qu = 'delete from student where Location = ?'
    vals = ('UK',)
    #vals = (name, sal, job)
    c = conn.cursor()
    c.execute(qu,vals)
    conn.commit()


if __name__ == '__main__':
    #database creation
    c = create_connection(r"D:\sample\pythonsamples\Database\student.db")
    #create table
    #if c is not None:
    #    create_table(c)
    #insert_data(c)
    #update_data(c)
    select_data(c)
    remove_data(c)
    print('after removal ...')
    select_data(c)
 