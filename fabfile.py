from fabric.api import local, lcd


def run():
    """ Run the development environment. """
    local('python app.py')


def build():
    local('cat static/css/style.css | cssmin > static/css/style.min.css')
    local('python app.py build')
    # Remove duplicate sitemap, move robots.txt to root directory.
    with lcd('build/static'):
        local('mv robots.txt ..; rm sitemap.xml')
    # GZIP CSS.
    with lcd('build/static/css'):
        local('for fn in *; do gzip < ${fn} > ${fn}.gz; done')


def deploy():
    build()
    local('ansible-playbook deployment/site.yml')
