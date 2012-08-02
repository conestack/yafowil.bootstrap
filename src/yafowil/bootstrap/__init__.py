import os
from yafowil.base import factory
try:
    # try to provide as fanstatic resource
    from js.bootstrap import bootstrap_responsive_css
    def register():
        import common
        factory.register_theme('bootstrap', 'yafowil.bootstrap',
                               css=[bootstrap_responsive_css])
except ImportError:
    # provide ourself if fanstatic not installed
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