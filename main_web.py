import web, os,sqlite3
from simpleCMSpy import admin_web

urls = (
    '/', 'Index',
    '/add', 'Add',
    '/setup', 'Setup'
)
app = web.application(urls, globals())
render = web.template.render('templates/', base='layout')

class Index(object):
    def GET(self):
        news = admin_web.read()
        if news != None:
            if len(news) != 0:
                return render.index(news = news)
            else:
                return render.index(news = None)
        else:
            return render.setup()

    def POST(self):
        form = web.input(author="unknown", title="no title", text=None)
        if form.author == "":
            form.author = "unknown"
        if form.title == "":
            form.title = "no title"
        if form.text != "":
            admin_web.add(form.title, form.text, form.author)
            news = admin_web.read()
        return render.index(news = news)


class Add(object):
    def GET(self):
        return render.add_form()

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
        conn = sqlite3.connect(db_filename)
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