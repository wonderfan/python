from flask import Flask,render_template,url_for,redirect,request,session,flash

from flask.ext import superadmin

# Create custom admin view
class MyAdminView(superadmin.AdminIndexView):
    @superadmin.expose('/')
    def index(self):
        return self.render('myadmin.html')

class ProxyAdminView(superadmin.BaseView):
    @superadmin.expose('/',methods=['GET', 'POST'])
    def index(self):
        if request.method=="POST":
            content = request.form['proxy']
            with open('proxy.info','w') as fw:
                fw.write(content)
        else:
            with open('proxy.info') as fr:
                content = fr.read()

        return self.render('proxy.html',data=content)
        
class CrawlAdminView(superadmin.BaseView):
    @superadmin.expose('/',methods=['GET','POST'])
    def index(self):
        if request.method == 'POST':
            url = request.form['url']
            if url is None or url == '':
                flash("The URL cant be empty!",'error')
            else:
                import subprocess
                import os
                os.system('cd /home/ubuntu/')
                subprocess.call(['scrapy','version'], shell=True)
                flash("Crawl the domain successuflly",'alert')
        else:
            url = ""
        return self.render('crawl.html',url=url)




# Create flask app
app = Flask(__name__, template_folder='templates')
app.secret_key = 'my_secret'

# Flask views
@app.route('/')
def index():
    return redirect('/admin/')


if __name__ == '__main__':
    # Create admin interface
    admin = superadmin.Admin(index_view=MyAdminView())
    admin.add_view(CrawlAdminView(name="Crawl"))
    admin.add_view(ProxyAdminView(name="Proxy"))
    admin.init_app(app)

    # Start app
    app.debug = True
    app.run(host='0.0.0.0',port=8080)
