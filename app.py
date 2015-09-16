import sys
from flask import Flask, request, send_from_directory
from flask import render_template
from flask_frozen import Freezer
from werkzeug.contrib.fixers import ProxyFix
from config import *
from helpers import get_blog_posts


app = Flask(__name__, static_folder='static')
freezer = Freezer(app)


# URL Generators for Flask Freezer
@freezer.register_generator
def blog_post():
    for post in get_blog_posts():
        yield {'title_slug': post['meta']['slug'][0]}


@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route('/')
def index():
    return render_template('index.html', name='index')

@app.route('/projects/')
def projects():
    return render_template('projects.html', name='projects')


@app.route('/ionic-horizontal-scroll-cards/')
def horizontal_slider_demo():
    return render_template('ionic-horizontal-scroll-cards.html', name='horizontal-scroll-cards')


@app.route('/blog/')
def blog():
    all_posts = get_blog_posts()
    return render_template('blog.html', name='blog', posts=all_posts)


@app.route('/blog/<title_slug>/')
def blog_post(title_slug):
    all_posts = get_blog_posts()
    post = [p for p in all_posts if p['meta']['slug'][0] == title_slug]
    return render_template('post.html', post=post[0])


app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run()
