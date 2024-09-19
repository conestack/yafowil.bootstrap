from yafowil.base import factory
from yafowil.bootstrap import bs3
from yafowil.bootstrap import bs4
from yafowil.bootstrap import bs5
from yafowil.utils import entry_point
import os
import warnings
import webresource as wr


resources_dir = os.path.join(os.path.dirname(__file__), 'resources')


##############################################################################
# Bootstrap 3
##############################################################################

# webresource ################################################################

bs3_resources_dir = os.path.join(resources_dir, 'bs3')
bs3_scripts_dir = os.path.join(bs3_resources_dir, 'js')
bs3_styles_dir = os.path.join(bs3_resources_dir, 'css')

bs3_resources = wr.ResourceGroup(
    name='yafowil.bootstrap',
    directory=bs3_resources_dir,
    path='bootstrap'
)
bs3_resources.add(wr.ScriptResource(
    name='bootstrap-js',
    depends='jquery-js',
    directory=bs3_scripts_dir,
    path='bootstrap/js',
    resource='bootstrap.js',
    compressed='bootstrap.min.js'
))
bs3_resources.add(wr.StyleResource(
    name='bootstrap-css',
    directory=bs3_styles_dir,
    path='bootstrap/css',
    resource='bootstrap.css',
    compressed='bootstrap.min.css'
))
bs3_resources.add(wr.StyleResource(
    name='bootstrap-theme-css',
    depends='bootstrap-css',
    directory=bs3_styles_dir,
    path='bootstrap/css',
    resource='bootstrap-theme.css',
    compressed='bootstrap-theme.min.css'
))

# B/C resources ##############################################################

js_bs3 = [{
    'group': 'bootstrap.dependencies',
    'resource': 'js/bootstrap.min.js',
    'order': 20
}]
css_bs3 = [{
    'group': 'bootstrap.dependencies',
    'resource': 'css/bootstrap.min.css',
    'order': 10
}, {
    'group': 'bootstrap.dependencies',
    'resource': 'css/bootstrap-theme.min.css',
    'order': 11,
}]


##############################################################################
# Bootstrap 4
##############################################################################

# webresource ################################################################

bs4_resources_dir = os.path.join(resources_dir, 'bs4')
bs4_scripts_dir = os.path.join(bs4_resources_dir, 'js')
bs4_styles_dir = os.path.join(bs4_resources_dir, 'css')

bs4_resources = wr.ResourceGroup(
    name='yafowil.bootstrap',
    directory=bs4_resources_dir,
    path='bootstrap',
)
bs4_resources.add(wr.ScriptResource(
    name='bootstrap-js',
    depends='jquery-js',
    directory=bs4_scripts_dir,
    path='bootstrap/js',
    resource='bootstrap.js',
    compressed='bootstrap.min.js'
))
bs4_resources.add(wr.StyleResource(
    name='bootstrap-css',
    directory=bs4_styles_dir,
    path='bootstrap/css',
    resource='bootstrap.css',
    compressed='bootstrap.min.css'
))

# B/C resources ##############################################################

js_bs4 = [{
    'group': 'bootstrap.dependencies',
    'resource': 'js/bootstrap.min.js',
    'order': 20
}]
css_bs4 = [{
    'group': 'bootstrap.dependencies',
    'resource': 'css/bootstrap.min.css',
    'order': 10
}]


##############################################################################
# Bootstrap 5
##############################################################################

# webresource ################################################################

bs5_resources_dir = os.path.join(resources_dir, 'bs5')
bs5_scripts_dir = os.path.join(bs5_resources_dir, 'js')
bs5_styles_dir = os.path.join(bs5_resources_dir, 'css')

bs5_resources = wr.ResourceGroup(
    name='yafowil.bootstrap',
    directory=bs5_resources_dir,
    path='bootstrap'
)
bs5_resources.add(wr.ScriptResource(
    name='bootstrap-js',
    directory=bs5_scripts_dir,
    path='bootstrap/js',
    resource='bootstrap.js',
    compressed='bootstrap.min.js'
))
bs5_resources.add(wr.StyleResource(
    name='bootstrap-css',
    directory=bs5_styles_dir,
    path='bootstrap/css',
    resource='bootstrap.css',
    compressed='bootstrap.min.css'
))
bs5_resources.add(wr.StyleResource(
    name='bootstrap-icons-css',
    directory=bs5_styles_dir,
    path='bootstrap/fonts',
    resource='bootstrap-icons.css'
))

# B/C resources ##############################################################

js_bs5 = [{
    'group': 'bootstrap.dependencies',
    'resource': 'js/bootstrap.min.js',
    'order': 20
}]
css_bs5 = [{
    'group': 'bootstrap.dependencies',
    'resource': 'css/bootstrap.min.css',
    'order': 10
}]


##############################################################################
# Registration
##############################################################################

@entry_point(order=20)
def register():
    widget_name = 'yafowil.bootstrap'

    # Bootstrap 3
    # bootstrap is legacy name for bootstrap3
    factory.register_theme(
        ['bootstrap', 'bootstrap3'],
        widget_name,
        bs3_resources_dir,
        js=js_bs3,
        css=css_bs3
    )
    factory.register_resources(
        ['bootstrap', 'bootstrap3'],
        widget_name,
        bs3_resources
    )

    # Bootstrap 4
    factory.register_theme(
        'bootstrap4',
        widget_name,
        bs4_resources_dir,
        js=js_bs4,
        css=css_bs4
    )
    factory.register_resources('bootstrap4', widget_name, bs4_resources)

    # Bootstrap 5
    factory.register_theme(
        'bootstrap5',
        widget_name,
        bs5_resources_dir,
        js=js_bs5,
        css=css_bs5
    )
    factory.register_resources('bootstrap5', widget_name, bs5_resources)


##############################################################################
# Configuration
##############################################################################

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
    baseline.configure_factory()
    baseline.register_macros()
