from yafowil.base import factory
from yafowil.utils import entry_point

import bs3
import bs4
import os


resourcedir_bs3 = os.path.join(os.path.dirname(__file__), "resources/bs3")
resourcedir_bs4 = os.path.join(os.path.dirname(__file__), "resources/bs4")

js_bs3 = [
    {"group": "bootstrap.dependencies", "resource": "js/bootstrap.js", "order": 20,}
]
css_bs3 = [
    {"group": "bootstrap.dependencies", "resource": "css/bootstrap.css", "order": 10,},
    {
        "group": "bootstrap.dependencies",
        "resource": "css/bootstrap-theme.css",
        "order": 11,
    },
]

js_bs4 = [
    {"group": "bootstrap.dependencies", "resource": "js/bootstrap.js", "order": 20,}
]
css_bs4 = [
    {"group": "bootstrap.dependencies", "resource": "css/bootstrap.css", "order": 10,}
]


@entry_point(order=20)
def register():
    # Bootstrap 3
    factory.register_theme(
        "bootstrap3", "yafowil.bootstrap", resourcedir_bs3, js=js_bs3, css=css_bs3
    )
    # BBB Bootstrap 3 - remove in next major release
    factory.register_theme(
        "bootstrap", "yafowil.bootstrap", resourcedir_bs3, js=js_bs3, css=css_bs3
    )
    # Bootstrap 4
    factory.register_theme(
        "bootstrap4", "yafowil.bootstrap", resourcedir_bs4, js=js_bs4, css=css_bs4
    )


def configure_factory(theme):
    """Configure the Yafowil factory with theme specific macros and defaults.
    """
    if theme == "bootstrap3":
        baseline = bs3
    elif theme == "bootstrap4":
        baseline = bs4
    else:
        raise ValueError("'theme' parameter must be one of: bootstrap3, bootstrap4")
    if os.environ.get("TESTRUN_MARKER"):
        # skip for testing
        # only configure factory if not suppressed explicit
        return
    baseline.configure_factory()
    baseline.register_macros()
