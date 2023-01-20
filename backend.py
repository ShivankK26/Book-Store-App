import concurrent.futures

import mysql.connector


def connect():
    conn = mysql.connector.connect(host="localhost",database='books',user="root",password="Shiv@123")#used to make connection
    cur = conn.cursor()#using cursor we can execute sql QUERIES
    cur.execute(#we can execute SQL queries using this
        'CREATE TABLE IF NOT EXISTS book (title varchar(15) , author varchar(15) , year integer , isbn integer)')


def insert(title, author, year, isbn):
    conn = mysql.connector.connect(host="localhost",database='books',user="root",password="Shiv@123")
    cur = conn.cursor()
    insert = ('INSERT INTO book(title,author,year,isbn) VALUES(%s,%s,%s,%s)')
    insert_var = (title, author, year, isbn)
    cur.execute(insert, insert_var)

    conn.commit()#it is required to make the changes otherwise no changes are made..


def view():
    conn = mysql.connector.connect(host="localhost",database='books',user="root",password="Shiv@123")
    cur = conn.cursor()
    cur.execute('SELECT * FROM book')
    rows = cur.fetchall()#fetch all rows from the result set..

    return rows


def search(title, author, year, isbn):
    conn = mysql.connector.connect(host="localhost",database='books',user="root",password="Shiv@123")
    cur = conn.cursor()
    selection = ('SELECT * FROM book WHERE title=%s OR author=%s OR year=%s OR isbn=%s')
    selection_var = (title, author, year, isbn)
    cur.execute(selection, selection_var)

    rows = cur.fetchall()

    return rows


connect()
insert('eww','ewew','1212','3232')
view()
search('eww','ewew','1212','3232')



