import os


def register():
    import yafowil.bootstrap.common


def get_resource_dir():
    return os.path.join(os.path.dirname(__file__), 'resources')


def get_css():
    return [{
        'resource': os.path.join('css', 'bootstrap.css'),
        'thirdparty': True,
        'order': 10,
    }, {
        'resource': os.path.join('css', 'bootstrap-responsive.css'),
        'thirdparty': True,
        'order': 11,
    }]
