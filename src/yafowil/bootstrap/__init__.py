import os
from yafowil.base import factory


resourcedir = os.path.join(os.path.dirname(__file__), 'resources')
js = [{
    'group': 'bootstrap.dependencies',
    'resource': 'js/bootstrap.js',
    'order': 20,
}]
css = [{
    'group': 'bootstrap.dependencies',
    'resource': 'css/bootstrap.css',
    'order': 10,
}, {
    'group': 'bootstrap.dependencies',
    'resource': 'css/bootstrap-theme.css',
    'order': 11,
}]


def register():
    import common
    factory.register_theme('bootstrap', 'yafowil.bootstrap',
                           resourcedir, js=js, css=css)
