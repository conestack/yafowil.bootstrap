from yafowil.base import factory
from yafowil.bootstrap import bs3
from yafowil.bootstrap import bs4
from yafowil.bootstrap import bs5
from yafowil.utils import entry_point
import os
import warnings


resources_dir = os.path.join(os.path.dirname(__file__), 'resources')


###############################################################################
# Bootstrap 3
###############################################################################

resources_bs3 = os.path.join(resources_dir, 'bs3')

js_bs3 = [{
    'group': 'bootstrap.dependencies',
    'resource': 'js/bootstrap.js',
    'order': 20
}]
css_bs3 = [{
    'group': 'bootstrap.dependencies',
    'resource': 'css/bootstrap.css',
    'order': 10
}, {
    'group': 'bootstrap.dependencies',
    'resource': 'css/bootstrap-theme.css',
    'order': 11,
}]


###############################################################################
# Bootstrap 4
###############################################################################

resources_bs4 = os.path.join(resources_dir, 'bs4')

js_bs4 = [{
    'group': 'bootstrap.dependencies',
    'resource': 'js/bootstrap.js',
    'order': 20
}]
css_bs4 = [{
    'group': 'bootstrap.dependencies',
    'resource': 'css/bootstrap.css',
    'order': 10
}]


###############################################################################
# Bootstrap 5
###############################################################################

resources_bs5 = os.path.join(resources_dir, 'bs5')

js_bs5 = [{
    'group': 'bootstrap.dependencies',
    'resource': 'js/bootstrap.js',
    'order': 20
}]
css_bs5 = [{
    'group': 'bootstrap.dependencies',
    'resource': 'css/bootstrap.css',
    'order': 10
}]


@entry_point(order=20)
def register():
    # Bootstrap 3
    # B/C bootstrap is legacy name for bootstrap3. remove in 3.0
    factory.register_theme(
        'bootstrap', 'yafowil.bootstrap', resources_bs3, js=js_bs3, css=css_bs3
    )
    factory.register_theme(
        'bootstrap3', 'yafowil.bootstrap', resources_bs3, js=js_bs3, css=css_bs3
    )
    # Bootstrap 4
    factory.register_theme(
        'bootstrap4', 'yafowil.bootstrap', resources_bs4, js=js_bs4, css=css_bs4
    )
    # Bootstrap 5
    factory.register_theme(
        'bootstrap5', 'yafowil.bootstrap', resources_bs5, js=js_bs5, css=css_bs5
    )


def configure_factory(theme):
    """Configure the Yafowil factory with theme specific macros and defaults.
    """
    if theme == 'bootstrap':
        warnings.warn(
            'Legacy ``bootstrap`` theme is deprecated. Please use '
            '``bootstrap3`` instead.'
        )
        baseline = bs3
    elif theme == 'bootstrap3':
        baseline = bs3
    elif theme == 'bootstrap4':
        baseline = bs4
    elif theme == 'bootstrap5':
        baseline = bs5
    else:
        raise ValueError('Available themes: bootstrap3, bootstrap4, bootstrap5')
    if os.environ.get('TESTRUN_MARKER'):
        # skip for testing
        # only configure factory if not suppressed explicit
        return
    baseline.configure_factory()
    baseline.register_macros()
