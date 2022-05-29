from node.tests import NodeTestCase
from yafowil.base import factory
import os
import unittest
import webresource as wr
import yafowil.loader  # noqa


def add_jquery_js(resources):
    resources.add(wr.ScriptResource(
        name='jquery-js',
        path='jquery',
        resource='jquery.js'
    ))


def np(path):
    return path.replace('/', os.path.sep)


class TestBootstrap(NodeTestCase):

    def test_bs3_resources(self):
        factory.theme = 'bootstrap'
        resources = factory.get_resources('yafowil.bootstrap', False)
        factory.theme = 'bootstrap3'
        self.assertTrue(
            factory.get_resources('yafowil.bootstrap', False) is resources
        )

        resources = factory.get_resources('yafowil.bootstrap')
        self.assertTrue(resources.directory.endswith(np('/resources/bs3')))
        self.assertEqual(resources.path, 'bootstrap')

        scripts = resources.scripts
        self.assertEqual(len(scripts), 1)

        self.assertTrue(scripts[0].directory.endswith(np('/bs3/js')))
        self.assertEqual(scripts[0].path, 'bootstrap/js')
        self.assertEqual(scripts[0].file_name, 'bootstrap.min.js')
        self.assertTrue(os.path.exists(scripts[0].file_path))

        styles = resources.styles
        self.assertEqual(len(styles), 2)

        self.assertTrue(styles[0].directory.endswith(np('/bs3/css')))
        self.assertEqual(styles[0].path, 'bootstrap/css')
        self.assertEqual(styles[0].file_name, 'bootstrap.min.css')
        self.assertTrue(os.path.exists(styles[0].file_path))

        self.assertTrue(styles[1].directory.endswith(np('/bs3/css')))
        self.assertEqual(styles[1].path, 'bootstrap/css')
        self.assertEqual(styles[1].file_name, 'bootstrap-theme.min.css')
        self.assertTrue(os.path.exists(styles[1].file_path))

        add_jquery_js(resources)
        resolver = wr.ResourceResolver(resources)
        renderer = wr.ResourceRenderer(resolver, base_url='')
        self.checkOutput("""
        <link href="/bootstrap/css/bootstrap.min.css" media="all"
              rel="stylesheet" type="text/css" />
        <link href="/bootstrap/css/bootstrap-theme.min.css" media="all"
              rel="stylesheet" type="text/css" />
        <script src="/jquery/jquery.js"></script>
        <script src="/bootstrap/js/bootstrap.min.js"></script>
        """, renderer.render())

    def test_bs4_resources(self):
        factory.theme = 'bootstrap4'
        resources = factory.get_resources('yafowil.bootstrap')
        self.assertTrue(resources.directory.endswith(np('/resources/bs4')))
        self.assertEqual(resources.path, 'bootstrap')

        scripts = resources.scripts
        self.assertEqual(len(scripts), 1)

        self.assertTrue(scripts[0].directory.endswith(np('/bs4/js')))
        self.assertEqual(scripts[0].path, 'bootstrap/js')
        self.assertEqual(scripts[0].file_name, 'bootstrap.min.js')
        self.assertTrue(os.path.exists(scripts[0].file_path))

        styles = resources.styles
        self.assertEqual(len(styles), 1)

        self.assertTrue(styles[0].directory.endswith(np('/bs4/css')))
        self.assertEqual(styles[0].path, 'bootstrap/css')
        self.assertEqual(styles[0].file_name, 'bootstrap.min.css')
        self.assertTrue(os.path.exists(styles[0].file_path))

        add_jquery_js(resources)
        resolver = wr.ResourceResolver(resources)
        renderer = wr.ResourceRenderer(resolver, base_url='')
        self.checkOutput("""
        <link href="/bootstrap/css/bootstrap.min.css" media="all"
              rel="stylesheet" type="text/css" />
        <script src="/jquery/jquery.js"></script>
        <script src="/bootstrap/js/bootstrap.min.js"></script>
        """, renderer.render())

    def test_bs5_resources(self):
        factory.theme = 'bootstrap5'
        resources = factory.get_resources('yafowil.bootstrap')
        self.assertTrue(resources.directory.endswith(np('/resources/bs5')))
        self.assertEqual(resources.path, 'bootstrap')

        scripts = resources.scripts
        self.assertEqual(len(scripts), 1)

        self.assertTrue(scripts[0].directory.endswith(np('/bs5/js')))
        self.assertEqual(scripts[0].path, 'bootstrap/js')
        self.assertEqual(scripts[0].file_name, 'bootstrap.min.js')
        self.assertTrue(os.path.exists(scripts[0].file_path))

        styles = resources.styles
        self.assertEqual(len(styles), 1)

        self.assertTrue(styles[0].directory.endswith(np('/bs5/css')))
        self.assertEqual(styles[0].path, 'bootstrap/css')
        self.assertEqual(styles[0].file_name, 'bootstrap.min.css')
        self.assertTrue(os.path.exists(styles[0].file_path))

        resolver = wr.ResourceResolver(resources)
        renderer = wr.ResourceRenderer(resolver, base_url='')
        self.checkOutput("""
        <script src="/bootstrap/js/bootstrap.min.js"></script>
        <link href="/bootstrap/css/bootstrap.min.css" media="all"
              rel="stylesheet" type="text/css" />
        """, renderer.render())

if __name__ == '__main__':
    unittest.main()
