import sqlite3
import time
import datetime
import random
from matplotlib import  pyplot as plt

conn = sqlite3.connect("myFirstdatabase.db")
cur = conn.cursor()


def create_Table():
    cur.execute('CREATE TABLE IF NOT EXISTS MYTABLE(id REAL, name TEXT, class TEXT, value REAL)')


def create_Table2():
    cur.execute('CREATE TABLE IF NOT EXISTS MYTABLE2(unix REAL, name TEXT, date TEXT, value REAL)')


def insert_Into():
    cur.execute("INSERT INTO MYTABLE VALUES(1, 'Rehan', 'Python', 8)")
    conn.commit()


def dynamicDataEntry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = "Python"
    value = random.randrange(0, 10)
    cur.execute("INSERT INTO MYTABLE2 (unix, name, date, value) VALUES (?, ?, ?, ?)", (unix, keyword, date, value))
    conn.commit()


def readFromdb():
    cur.execute("SELECT * FROM MYTABLE2")
    data = cur.fetchall()
    for row in data:
        print(row)


def readForValue():
    cur.execute("SELECT * FROM MYTABLE2 WHERE value='3'")
    data = cur.fetchall()
    for row in data:
        print(row)


def plotDatainGraph():
    cur.execute('SELECT unix, value FROM MYTABLE2')
    dates = []
    values = []
    for row in cur.fetchall():
        date = row[0]
        value = row[1]
        dates.append(datetime.datetime.fromtimestamp(date))
        values.append(value)
    plt.title("Database graph")
    plt.xlabel('dates')
    plt.ylabel('values')
    plt.plot_date(dates, values, '-')
    plt.show()

def updateColoumns():
    # please change value in where clause after delele statement execution
    cur.execute('UPDATE MYTABLE2 SET value = 99 WHERE value = 3.0')
    conn.commit()

    cur.execute('SELECT * FROM MYTABLE2')
    [print(row) for row in cur.fetchall()]

def deleteRows():
    cur.execute('DELETE FROM MYTABLE2 WHERE value = 99')
    conn.commit()

    cur.execute('SELECT * FROM MYTABLE2')
    [print(row) for row in cur.fetchall()]
# create_Table()
# create_Table2()
# for x in range(10):
#    dynamicDataEntry()
#    time.sleep(1)

# insert_Into()
#readFromdb()
#readForValue()
#plotDatainGraph()
#updateColoumns()
deleteRows()
cur.close()
conn.close()
