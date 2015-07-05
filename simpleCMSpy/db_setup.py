import sqlite3, os, getpass, time

def setup():
    print "Welcome to simpleCMSpy - %s\n" % time.strftime("%d/%m/%Y")
    if not os.path.exists("database/simpleCMS.db"):
        print "\tThis is the initial DB setup\n" \
              "\tbe ready to iput some data for us.\n"
        print "\tCreating database..",
        db_filename = "database/simpleCMS.db"
        schema_filename = "database/schema.sql"
        conn = sqlite3.connect(db_filename)
        print "done!"
        print "\tCreating schema..",
        f = open(schema_filename, 'rt')
        schema = f.read()
        conn.executescript(schema)
        print "done!"
        print "\n\tWe now need to create a user account." \
              "\n\tYou'll be able to add/remove users later," \
              "\n\tbut at least one user account is mandatory\n"
        user_name = raw_input("\tSelect a user name: ")
        password = hash(getpass.getpass("\tSelect a password: "))
        query = "insert into users (name,password) values ('%s','%i')" % (user_name,password)
        conn.execute(query)
        conn.commit()
        conn.close()
        print ""
