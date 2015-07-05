import sqlite3 as db
import getpass,time,os, web

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
        cursor.execute("select title,author,date,content,id from news")
        news = cursor.fetchall()
        conn.close()
        return news

def login(user_name, password):
    conn = db.connect("database/simpleCMS.db")
    cursor = conn.cursor()
    cursor.execute("select password from users where name = ?",(user_name,))
    hashed_pw = cursor.fetchone()
    conn.close()
    if hashed_pw is not None:
        hashed_pw = hashed_pw[0]
        if hashed_pw == hash(password):
            # we need more security, this is spoof prone.. (TODO: session cookie..)
            web.setcookie('user_name', user_name, 3600)
            return True
    return False

def rem(n):
    conn = db.connect("database/simpleCMS.db")
    query = "delete from news where id = '%i'" % int(n)
    conn.execute(query)
    conn.commit()
    conn.close()
