import sqlite3 as db
import getpass,time

def login():
    print "\t--- LOGIN ---"
    conn = db.connect("database/simpleCMS.db")
    cursor = conn.cursor()
    name = raw_input("\tusername: ")
    passw = hash(getpass.getpass("\tpassword: "))
    cursor.execute("select password from users where name = ?",(name,))
    hashed_pw = cursor.fetchone()[0]
    conn.close()
    if passw == hashed_pw:
        print "\tWelcome %s\n" % name
        return name
    else:
        print "\tinvalid username/password"
        return "guest"

def add(user):
    title = raw_input("Title: ")
    content = raw_input("Content: ")
    date = time.strftime("%d-%m-%Y")
    query = "insert into news (title,content,date,author) " \
            "values ('%s','%s','%s','%s')" % (title,content,date,user)
    conn = db.connect("database/simpleCMS.db")
    conn.execute(query)
    conn.commit()

def rem(n):
    conn = db.connect("database/simpleCMS.db")
    query = "delete from news where id = '%i'" % n
    conn.execute(query)
    conn.commit()
    conn.close()

def titles():
    conn = db.connect("database/simpleCMS.db")
    cursor = conn.cursor()
    cursor.execute("select id,title,date from news")
    titles = cursor.fetchall()
    for title in titles:
        print "%s - %s (%s)" % (title[0], title[1], title[2])
    conn.close()

def read(n):
    conn = db.connect("database/simpleCMS.db")
    cursor = conn.cursor()
    cursor.execute("select title,author,date,content from news where id = ?",(n,))
    news = cursor.fetchone()
    if news:
        print "\n~%s~" % insert_newlines(news[0].upper().center(40), every=42)
        print "------------------------------------------"
        subtitle = "by %s%s" % (news[1].ljust(29), news[2].rjust(10))
        print subtitle
        print "------------------------------------------"
        print insert_newlines(news[3])
        print "\n"
    conn.close()

def insert_newlines(string, every=42):
    lines = []
    for i in xrange(0, len(string), every):
        lines.append(string[i:i+every])
    return '\n'.join(lines)