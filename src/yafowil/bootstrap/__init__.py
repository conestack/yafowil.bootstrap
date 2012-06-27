import os
from yafowil.base import factory


resourcedir = os.path.join(os.path.dirname(__file__), 'resources')

css = [{
    'resource': os.path.join('css', 'bootstrap.css'),
    'thirdparty': True,
    'order': 10,
}, {
    'resource': os.path.join('css', 'bootstrap-responsive.css'),
    'thirdparty': True,
    'order': 11,
}]


def register():
    import common    
    factory.register_theme('bootstrap', 'yafowil.bootstrap',
                           resourcedir, css=css)