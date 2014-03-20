from fabric.api import local


def compress_static():
    local('cat static/css/style.css | cssmin > static/css/style.min.css')
