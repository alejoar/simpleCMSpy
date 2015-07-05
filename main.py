from simpleCMSpy import db_setup, admin

commands = ["login", "add", "remove", "titles", "read"]

db_setup.setup()
user = "guest"
input = [""]

def help():
    print "Commands are:",
    for c in commands:
        print "%s," % c,
    print "..\n"

help()

while input[0] != "exit":
    command = raw_input("%s@simpleCMSpy> " % user)
    input = command.split()

    if input[0] == "help":
        help()

    elif input[0] == "login":
        if user != "guest":
            print "You are already logged in\n"
        else:
            user = admin.login()

    elif input[0] == "add":
        if user != "guest":
            admin.add(user)
        else:
            print "access denied\n"

    elif input[0] in ["remove", "delete"]:
        if user != "guest":
            admin.rem(int(input[1]))
        else:
            print "access denied\n"

    elif input[0] == "titles":
        admin.titles()

    elif input[0] == "read":
        admin.read(int(input[1]))

    else:
        print "Unknown command. Use 'help' for a list\n"
