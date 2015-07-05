import web, os, sqlite3 as db
from simpleCMSpy import admin_web

urls = (
    '/', 'Index',
    '/add', 'Add',
    '/setup', 'Setup',
    '/login', 'Login',
    '/logout', 'Logout',
    '/rem', 'Rem'
)
app = web.application(urls, globals())
render = web.template.render('templates/', base='layout')

def user_is_admin():
    cookie = web.cookies(user_name=None)
    if cookie.user_name is not None:
        return True
    return False

class Index(object):
    def GET(self):
        news = admin_web.read()
        cookie = web.cookies(user_name=None)

        if news is not None:
            if len(news) == 0:
                news = None
            return render.index(news = news, user_name = cookie.user_name)

        else:
            return render.setup()

class Login(object):
    def GET(self):
        return render.login(error=None)

    def POST(self):
        form = web.input(user_name=None, password=None)
        if form.user_name and form.password:
            if admin_web.login(form.user_name,form.password):
                raise web.seeother('/')
            else:
                return render.login(error="wrong user name or password")
        else:
            return render.login(error="fill both fields..")

class Logout(object):
    def GET(self):
        web.setcookie('user_name', "", -1)
        raise web.seeother('/')

class Add(object):
    def GET(self):
        return render.add_form()

    def POST(self):
        form = web.input(author="unknown", title="no title", text=None)
        if form.author == "":
            form.author = "unknown"
        if form.title == "":
            form.title = "no title"
        if form.text != "":
            admin_web.add(form.title, form.text, form.author)
        raise web.seeother('/')

class Rem(object):
    def GET(self):
        user_data = web.input()
        if user_is_admin():
            admin_web.rem(user_data.id)
        raise web.seeother('/')

class Setup(object):
    def GET(self):
        if os.path.isfile("database/simpleCMS.db"):
            return render.setup_done()
        else:
            return "something went wrong.. (or maybe you shouldn't be here)"

    def POST(self):
        if os.path.isfile("database/simpleCMS.db"):
            return Index.GET()

        form = web.input(user_name=None, password=None)
        db_filename = "database/simpleCMS.db"
        schema_filename = "database/schema.sql"
        conn = db.connect(db_filename)
        f = open(schema_filename, 'rt')
        schema = f.read()
        conn.executescript(schema)
        query = "insert into users (name,password) values ('%s','%i')" % (form.user_name,hash(form.password))
        conn.execute(query)
        conn.commit()
        conn.close()
        return render.setup_done()

if __name__ == "__main__":
    app.run()