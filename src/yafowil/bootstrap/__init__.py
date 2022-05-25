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

bs3_scripts = wr.ResourceGroup(
    name='yafowil-bootstrap-scripts',
    path='yafowil.bootstrap'
)
bs3_scripts.add(wr.ScriptResource(
    name='bootstrap-js',
    depends='jquery-js',
    directory=bs3_scripts_dir,
    resource='bootstrap.js',
    compressed='bootstrap.min.js'
))

bs3_styles = wr.ResourceGroup(
    name='yafowil-bootstrap-styles',
    path='yafowil.bootstrap'
)
bs3_styles.add(wr.StyleResource(
    name='bootstrap-css',
    directory=bs3_styles_dir,
    resource='bootstrap.css',
    compressed='bootstrap.min.css'
))
bs3_styles.add(wr.StyleResource(
    name='bootstrap-theme-css',
    depends='bootstrap-css',
    directory=bs3_styles_dir,
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

bs4_scripts = wr.ResourceGroup(
    name='yafowil-bootstrap-scripts',
    path='yafowil.bootstrap'
)
bs4_scripts.add(wr.ScriptResource(
    name='bootstrap-js',
    depends='jquery-js',
    directory=bs4_scripts_dir,
    resource='bootstrap.js',
    compressed='bootstrap.min.js'
))

bs4_styles = wr.ResourceGroup(
    name='yafowil-bootstrap-styles',
    path='yafowil.bootstrap'
)
bs4_styles.add(wr.StyleResource(
    name='bootstrap-css',
    directory=bs4_styles_dir,
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

bs5_scripts = wr.ResourceGroup(
    name='yafowil-bootstrap-scripts',
    path='yafowil.bootstrap'
)
bs5_scripts.add(wr.ScriptResource(
    name='bootstrap-js',
    directory=bs5_scripts_dir,
    resource='bootstrap.js',
    compressed='bootstrap.min.js'
))

bs5_styles = wr.ResourceGroup(
    name='yafowil-bootstrap-styles',
    path='yafowil.bootstrap'
)
bs5_styles.add(wr.StyleResource(
    name='bootstrap-css',
    directory=bs5_styles_dir,
    resource='bootstrap.css',
    compressed='bootstrap.min.css'
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
    # Bootstrap 3
    # B/C bootstrap is legacy name for bootstrap3
    factory.register_theme(
        ['bootstrap', 'bootstrap3'], 'yafowil.bootstrap', bs3_resources_dir,
        js=js_bs3, css=css_bs3
    )
    factory.register_scripts(
        ['bootstrap', 'bootstrap3'],
        'yafowil.bootstrap',
        bs3_scripts
    )
    factory.register_styles(
        ['bootstrap', 'bootstrap3'],
        'yafowil.bootstrap',
        bs3_styles
    )

    # Bootstrap 4
    factory.register_theme(
        'bootstrap4', 'yafowil.bootstrap', bs4_resources_dir,
        js=js_bs4, css=css_bs4
    )
    factory.register_scripts('bootstrap4', 'yafowil.bootstrap', bs4_scripts)
    factory.register_styles('bootstrap4', 'yafowil.bootstrap', bs4_styles)

    # Bootstrap 5
    factory.register_theme(
        'bootstrap5', 'yafowil.bootstrap', bs5_resources_dir,
        js=js_bs5, css=css_bs5
    )
    factory.register_scripts('bootstrap5', 'yafowil.bootstrap', bs5_scripts)
    factory.register_styles('bootstrap5', 'yafowil.bootstrap', bs5_styles)


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
