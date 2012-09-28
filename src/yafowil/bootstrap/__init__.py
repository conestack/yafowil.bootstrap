import os
from yafowil.base import factory


resourcedir = os.path.join(os.path.dirname(__file__), 'resources')
css = [{
    'group': 'bootstrap',
    'resource': os.path.join('css', 'bootstrap.css'),
    'order': 10,
}, {
    'group': 'bootstrap',
    'resource': os.path.join('css', 'bootstrap-responsive.css'),
    'order': 11,
}]


def register():
    import common
    factory.register_theme('bootstrap', 'yafowil.bootstrap',
                           resourcedir, css=css)