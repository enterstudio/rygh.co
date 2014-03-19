from flask import Flask, request, send_from_directory
from flask import render_template
from werkzeug.contrib.fixers import ProxyFix
import json

app = Flask(__name__, static_folder='static')


@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route('/')
def index():
    return render_template('index.html', name='index')


@app.route('/blog/')
def blog():
    df = open('posts.json').read()
    posts = json.loads(df)
    return render_template('blog/blog.html', name='blog', posts=posts)


@app.route('/blog/<title_slug>')
def blog_post(title_slug):
    df = open('posts.json').read()
    posts = json.loads(df)
    fp = [p for p in posts if p['title_slug'] == title_slug][0]
    return render_template(fp['file'], post=p)


app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run()
