import sqlite3 as db
import getpass,time,os

def add(title,content,user):
    date = time.strftime("%d-%m-%Y")
    print "adding new entry %s %s %s %s" % (title,content,date,user)
    query = "insert into news (title,content,date,author) " \
            "values ('%s','%s','%s','%s')" % (title,content,date,user)
    conn = db.connect("database/simpleCMS.db")
    conn.execute(query)
    conn.commit()

def read():
    if not os.path.isfile("database/simpleCMS.db"):
        return None
    else:
        conn = db.connect("database/simpleCMS.db")
        cursor = conn.cursor()
        cursor.execute("select title,author,date,content from news")
        news = cursor.fetchall()
        conn.close()
        return news
