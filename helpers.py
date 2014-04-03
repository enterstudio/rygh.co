import os
import markdown
import codecs
from preprocessors import preprocess


def get_blog_posts():
    """
    Returns a list of dictionaries that contain content
    of a blog post, and metadata about the post.
    """

    file_names = os.listdir('content/')
    posts = []

    for f in file_names:
        md = markdown.Markdown(extensions=['meta'])
        content = preprocess(codecs.open('content/%s' % f, 'r', 'utf8').read())
        html = md.convert(content)
        meta_data = md.Meta
        posts.append({'meta': meta_data, 'content': html})

    return posts
