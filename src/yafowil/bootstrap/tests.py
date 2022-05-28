from node.tests import NodeTestCase
from yafowil.base import factory
import copy
import unittest
import webresource as wr
import yafowil.loader  # noqa


def add_jquery_js(resources):
    resources.add(wr.ScriptResource(
        name='jquery-js',
        path='dependencies',
        resource='jquery.js'
    ))


class TestBootstrap(NodeTestCase):

    def test_bs3_resources(self):
        factory.theme = 'bootstrap'
        resources = factory.get_resources('yafowil.bootstrap')
        add_jquery_js(resources)

        resolver = wr.ResourceResolver(resources)
        renderer = wr.ResourceRenderer(resolver, base_url='')

        self.checkOutput("""
        <link href="/bootstrap/css/bootstrap.min.css" media="all"
              rel="stylesheet" type="text/css" />
        <link href="/bootstrap/css/bootstrap-theme.min.css" media="all"
              rel="stylesheet" type="text/css" />
        <script src="/dependencies/jquery.js"></script>
        <script src="/bootstrap/js/bootstrap.min.js"></script>
        """, renderer.render())

        factory.theme = 'bootstrap3'
        resources = factory.get_resources('yafowil.bootstrap')
        add_jquery_js(resources)

        resolver = wr.ResourceResolver(resources)
        renderer = wr.ResourceRenderer(resolver, base_url='')

        self.checkOutput("""
        <link href="/bootstrap/css/bootstrap.min.css" media="all"
              rel="stylesheet" type="text/css" />
        <link href="/bootstrap/css/bootstrap-theme.min.css" media="all"
              rel="stylesheet" type="text/css" />
        <script src="/dependencies/jquery.js"></script>
        <script src="/bootstrap/js/bootstrap.min.js"></script>
        """, renderer.render())

        self.assertTrue(resources.directory.endswith('/resources/bs3'))
        self.assertEqual(resources.path, 'bootstrap')

        scripts = resources.scripts
        self.assertEqual(len(scripts), 2)

        styles = resources.styles
        self.assertEqual(len(styles), 2)

    def test_bs4_resources(self):
        factory.theme = 'bootstrap4'
        resources = factory.get_resources('yafowil.bootstrap')
        add_jquery_js(resources)

        resolver = wr.ResourceResolver(resources)
        renderer = wr.ResourceRenderer(resolver, base_url='')

        self.checkOutput("""
        <link href="/bootstrap/css/bootstrap.min.css" media="all"
              rel="stylesheet" type="text/css" />
        <script src="/dependencies/jquery.js"></script>
        <script src="/bootstrap/js/bootstrap.min.js"></script>
        """, renderer.render())

    def test_bs5_resources(self):
        factory.theme = 'bootstrap5'
        resources = factory.get_resources('yafowil.bootstrap')

        resolver = wr.ResourceResolver(resources)
        renderer = wr.ResourceRenderer(resolver, base_url='')

        self.checkOutput("""
        <script src="/bootstrap/js/bootstrap.min.js"></script>
        <link href="/bootstrap/css/bootstrap.min.css" media="all"
              rel="stylesheet" type="text/css" />
        """, renderer.render())

if __name__ == '__main__':
    unittest.main()
