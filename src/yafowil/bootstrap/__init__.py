from yafowil.base import factory
from yafowil.bootstrap.common import configure_factory
from yafowil.bootstrap.common import register_macros
from yafowil.utils import entry_point
import os


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


@entry_point(order=20)
def register():
    factory.register_theme('bootstrap', 'yafowil.bootstrap',
                           resourcedir, js=js, css=css)


@entry_point(order=20)
def configure():
    # only configure factory if not suppressed explicit
    if not os.environ.get('TESTRUN_MARKER'):
        configure_factory()
        register_macros()
