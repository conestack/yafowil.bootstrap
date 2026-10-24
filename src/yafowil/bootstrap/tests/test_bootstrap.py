from yafowil.base import factory
from yafowil.bootstrap import configure_factory
from yafowil.bootstrap import register
from yafowil.bootstrap.bs3 import bs_field_class
from yafowil.tests import fxml
from yafowil.tests import YafowilTestCase
import os
import warnings
import webresource as wr


def add_jquery_js(resources):
    resources.add(
        wr.ScriptResource(name='jquery-js', path='jquery', resource='jquery.js')
    )


def np(path):
    return path.replace('/', os.path.sep)


def text_field():
    return factory(
        '#field:text',
        name='text',
        props={'label': 'Text', 'help': 'Help', 'required': 'Required'},
    )


def select_field(**props):
    props.update(label='Select', vocabulary=[('a', 'A'), ('b', 'B')])
    return factory('#field:select', name='select', props=props)


class BootstrapTestCase(YafowilTestCase):
    """``YafowilTestCase`` pushes and clears the global factory state on setup
    and pops it on teardown. This keeps theme, defaults, macros and docs
    changed by ``configure_factory`` from leaking into other tests.
    """

    def setUp(self):
        super(BootstrapTestCase, self).setUp()
        register()


class TestResources(BootstrapTestCase):
    def test_bs3_resources(self):
        factory.theme = 'bootstrap'
        resources = factory.get_resources('yafowil.bootstrap', False)
        factory.theme = 'bootstrap3'
        self.assertTrue(factory.get_resources('yafowil.bootstrap', False) is resources)

        resources = factory.get_resources('yafowil.bootstrap')
        self.assertTrue(resources.directory.endswith(np('/resources/bs3')))
        self.assertEqual(resources.name, 'yafowil.bootstrap')
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
        self.checkOutput(
            """
        <link href="/bootstrap/css/bootstrap.min.css" media="all"
              rel="stylesheet" type="text/css" />
        <link href="/bootstrap/css/bootstrap-theme.min.css" media="all"
              rel="stylesheet" type="text/css" />
        <script src="/jquery/jquery.js"></script>
        <script src="/bootstrap/js/bootstrap.min.js"></script>
        """,
            renderer.render(),
        )

    def test_bs4_resources(self):
        factory.theme = 'bootstrap4'
        resources = factory.get_resources('yafowil.bootstrap')
        self.assertEqual(resources.name, 'yafowil.bootstrap')
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
        self.checkOutput(
            """
        <link href="/bootstrap/css/bootstrap.min.css" media="all"
              rel="stylesheet" type="text/css" />
        <script src="/jquery/jquery.js"></script>
        <script src="/bootstrap/js/bootstrap.min.js"></script>
        """,
            renderer.render(),
        )

    def test_bs5_resources(self):
        factory.theme = 'bootstrap5'
        resources = factory.get_resources('yafowil.bootstrap')
        self.assertEqual(resources.name, 'yafowil.bootstrap')
        self.assertTrue(resources.directory.endswith(np('/resources/bs5')))
        self.assertEqual(resources.path, 'bootstrap')

        scripts = resources.scripts
        self.assertEqual(len(scripts), 2)

        self.assertTrue(scripts[0].directory.endswith(np('/bs5/js')))
        self.assertEqual(scripts[0].path, 'bootstrap/js')
        self.assertEqual(scripts[0].file_name, 'popper.min.js')
        self.assertTrue(os.path.exists(scripts[0].file_path))

        self.assertTrue(scripts[1].directory.endswith(np('/bs5/js')))
        self.assertEqual(scripts[1].path, 'bootstrap/js')
        self.assertEqual(scripts[1].file_name, 'bootstrap.min.js')
        self.assertTrue(os.path.exists(scripts[1].file_path))

        styles = resources.styles
        self.assertEqual(len(styles), 2)

        self.assertTrue(styles[0].directory.endswith(np('/bs5/css')))
        self.assertEqual(styles[0].path, 'bootstrap/css')
        self.assertEqual(styles[0].file_name, 'bootstrap.min.css')
        self.assertTrue(os.path.exists(styles[0].file_path))

        self.assertTrue(styles[1].directory.endswith(np('/bs5/fonts')))
        self.assertEqual(styles[1].path, 'bootstrap/fonts')
        self.assertEqual(styles[1].file_name, 'bootstrap-icons.css')
        self.assertTrue(os.path.exists(styles[1].file_path))

        resolver = wr.ResourceResolver(resources)
        renderer = wr.ResourceRenderer(resolver, base_url='')
        self.checkOutput(
            """
        <script src="/bootstrap/js/popper.min.js"></script>
        <script src="/bootstrap/js/bootstrap.min.js"></script>
        <link href="/bootstrap/css/bootstrap.min.css" media="all"
              rel="stylesheet" type="text/css" />
        <link href="/bootstrap/fonts/bootstrap-icons.css" media="all"
              rel="stylesheet" type="text/css" />
        """,
            renderer.render(),
        )


class TestConfigureFactory(BootstrapTestCase):
    def test_bootstrap3_sets_bootstrap3_theme(self):
        configure_factory('bootstrap3')
        self.assertEqual(factory.theme, 'bootstrap3')

    def test_bootstrap4_sets_bootstrap4_theme(self):
        configure_factory('bootstrap4')
        self.assertEqual(factory.theme, 'bootstrap4')

    def test_bootstrap5_sets_bootstrap5_theme(self):
        configure_factory('bootstrap5')
        self.assertEqual(factory.theme, 'bootstrap5')

    def test_legacy_bootstrap_warns_deprecation(self):
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter('always')
            configure_factory('bootstrap')
        self.assertEqual(
            [str(warning.message) for warning in caught],
            [
                'Legacy ``bootstrap`` theme is deprecated. Please use '
                '``bootstrap3`` instead.'
            ],
        )

    def test_legacy_bootstrap_sets_bootstrap3_theme(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            configure_factory('bootstrap')
        self.assertEqual(factory.theme, 'bootstrap3')

    def test_unknown_theme_raises_value_error(self):
        with self.assertRaises(ValueError) as arc:
            configure_factory('unknown')
        self.assertEqual(
            str(arc.exception), 'Available themes: bootstrap3, bootstrap4, bootstrap5'
        )


class TestBootstrap3(BootstrapTestCase):
    def setUp(self):
        super(TestBootstrap3, self).setUp()
        configure_factory('bootstrap3')

    def test_text_field_renders_horizontal_form_group(self):
        self.checkOutput(
            """
        <div class="form-group" id="field-text">
          <label class="col-sm-2 control-label" for="input-text">Text</label>
          <div class="col-sm-10">
            <input class="form-control required text" id="input-text"
                   name="text" required="required" type="text" value=""/>
            <p class="help-block">Help</p>
          </div>
        </div>
        """,
            fxml(text_field()()),
        )

    def test_text_field_with_error_renders_has_error_and_help_block(self):
        widget = text_field()
        data = widget.extract({'text': ''})
        self.checkOutput(
            """
        <div class="form-group has-error" id="field-text">
          <label class="col-sm-2 control-label" for="input-text">Text</label>
          <div class="col-sm-10">
            <input class="form-control required text" id="input-text"
                   name="text" required="required" type="text" value=""/>
            <span class="help-block">
              <div class="text-danger">Required</div>
            </span>
            <p class="help-block">Help</p>
          </div>
        </div>
        """,
            fxml(widget(data=data)),
        )

    def test_select_renders_form_control(self):
        self.checkOutput(
            """
        <div class="form-group" id="field-select">
          <label class="col-sm-2 control-label"
                 for="input-select">Select</label>
          <div class="col-sm-10">
            <select class="form-control select" id="input-select"
                    name="select">
              <option id="input-select-a" value="a">A</option>
              <option id="input-select-b" value="b">B</option>
            </select>
          </div>
        </div>
        """,
            fxml(select_field()()),
        )

    def test_single_listing_select_renders_radio_wrapper(self):
        self.checkOutput(
            """
        <div class="form-group" id="field-select">
          <label class="col-sm-2 control-label"
                 for="input-select">Select</label>
          <div class="col-sm-10">
            <input id="exists-select" name="select-exists" type="hidden"
                   value="exists"/>
            <div id="radio-select-wrapper">
              <div class="radio" id="radio-select-a">
                <label for="input-select-a"><input class="select"
                  id="input-select-a" name="select" type="radio"
                  value="a"/>A</label>
              </div>
              <div class="radio" id="radio-select-b">
                <label for="input-select-b"><input class="select"
                  id="input-select-b" name="select" type="radio"
                  value="b"/>B</label>
              </div>
            </div>
          </div>
        </div>
        """,
            fxml(select_field(format='single')()),
        )

    def test_multivalued_listing_select_renders_checkbox_wrapper(self):
        widget = select_field(format='single', multivalued=True)
        self.checkOutput(
            """
        <div class="form-group" id="field-select">
          <label class="col-sm-2 control-label"
                 for="input-select">Select</label>
          <div class="col-sm-10">
            <input id="exists-select" name="select-exists" type="hidden"
                   value="exists"/>
            <div id="checkbox-select-wrapper">
              <div class="checkbox" id="checkbox-select-a">
                <label for="input-select-a"><input class="select"
                  id="input-select-a" name="select" type="checkbox"
                  value="a"/>A</label>
              </div>
              <div class="checkbox" id="checkbox-select-b">
                <label for="input-select-b"><input class="select"
                  id="input-select-b" name="select" type="checkbox"
                  value="b"/>B</label>
              </div>
            </div>
          </div>
        </div>
        """,
            fxml(widget()),
        )

    def test_button_macro_renders_default_submit_button(self):
        widget = factory('#button', name='button', props={'label': 'Button'})
        self.checkOutput(
            """
        <input class="btn btn-default" id="input-button" name="action.button"
               type="submit" value="Button"/>
        """,
            fxml(widget()),
        )

    def test_form_macro_renders_horizontal_form(self):
        widget = factory('#form', name='form', props={'action': 'action'})
        self.checkOutput(
            """
        <form action="action" class="form-horizontal"
              enctype="multipart/form-data" id="form-form" method="post"
              novalidate="novalidate"/>
        """,
            fxml(widget()),
        )

    def test_arrayfield_macro_renders_form_group_without_columns(self):
        widget = factory(
            '#arrayfield:text', name='text', props={'label': 'Text', 'help': 'Help'}
        )
        self.checkOutput(
            """
        <div class="form-group" id="field-text">
          <label class="control-label" for="input-text">Text</label>
          <input class="form-control text" id="input-text" name="text"
                 type="text" value=""/>
          <p class="help-block">Help</p>
        </div>
        """,
            fxml(widget()),
        )

    def test_array_macro_places_array_in_horizontal_columns(self):
        # yafowil.widget.array is no dependency, hence check registration
        self.assertEqual(
            factory._macros['array'],
            (
                ['field', 'label', 'help', 'error', 'array'],
                {
                    'array.label': ' ',
                    'field.class': bs_field_class,
                    'label.class_add': 'col-sm-2',
                    'array.class_add': 'col-sm-10',
                    'help.class_add': 'col-sm-offset-2 col-sm-10',
                    'error.class_add': 'col-sm-offset-2 col-sm-10',
                },
            ),
        )


class TestBootstrap4(BootstrapTestCase):
    def setUp(self):
        super(TestBootstrap4, self).setUp()
        configure_factory('bootstrap4')

    def test_text_field_renders_form_group(self):
        self.checkOutput(
            """
        <div class="form-group" id="field-text">
          <label class="required" for="input-text">Text</label>
          <input class="form-control required" id="input-text" name="text"
                 required="required" type="text" value=""/>
          <small class="form-text text-muted">Help</small>
        </div>
        """,
            fxml(text_field()()),
        )

    def test_text_field_with_error_renders_invalid_feedback(self):
        widget = text_field()
        data = widget.extract({'text': ''})
        self.checkOutput(
            """
        <div class="form-group" id="field-text">
          <label class="required" for="input-text">Text</label>
          <input class="form-control is-invalid required" id="input-text"
                 name="text" required="required" type="text" value=""/>
          <div class="invalid-feedback">Required</div>
          <small class="form-text text-muted">Help</small>
        </div>
        """,
            fxml(widget(data=data)),
        )

    def test_text_field_with_valid_value_renders_is_valid(self):
        widget = text_field()
        data = widget.extract({'text': 'value'})
        self.checkOutput(
            """
        <div class="form-group" id="field-text">
          <label class="required" for="input-text">Text</label>
          <input class="form-control is-valid required" id="input-text"
                 name="text" required="required" type="text" value="value"/>
          <small class="form-text text-muted">Help</small>
        </div>
        """,
            fxml(widget(data=data)),
        )

    def test_select_renders_form_control(self):
        self.checkOutput(
            """
        <div class="form-group" id="field-select">
          <label for="input-select">Select</label>
          <select class="form-control select" id="input-select" name="select">
            <option id="input-select-a" value="a">A</option>
            <option id="input-select-b" value="b">B</option>
          </select>
        </div>
        """,
            fxml(select_field()()),
        )

    def test_single_listing_select_renders_form_check_radios(self):
        self.checkOutput(
            """
        <div class="form-group" id="field-select">
          <label for="input-select">Select</label>
          <input id="exists-select" name="select-exists" type="hidden"
                 value="exists"/>
          <div id="radio-select-wrapper">
            <div class="form-check" id="radio-select-a">
              <input class="form-check-input select" id="input-select-a"
                     name="select" type="radio" value="a"/>
              <label class="form-check-label" for="input-select-a">A</label>
            </div>
            <div class="form-check" id="radio-select-b">
              <input class="form-check-input select" id="input-select-b"
                     name="select" type="radio" value="b"/>
              <label class="form-check-label" for="input-select-b">B</label>
            </div>
          </div>
        </div>
        """,
            fxml(select_field(format='single')()),
        )

    def test_multivalued_listing_select_renders_form_check_checkboxes(self):
        widget = select_field(format='single', multivalued=True)
        self.checkOutput(
            """
        <div class="form-group" id="field-select">
          <label for="input-select">Select</label>
          <input id="exists-select" name="select-exists" type="hidden"
                 value="exists"/>
          <div id="checkbox-select-wrapper">
            <div class="form-check" id="checkbox-select-a">
              <input class="form-check-input select" id="input-select-a"
                     name="select" type="checkbox" value="a"/>
              <label class="form-check-label" for="input-select-a">A</label>
            </div>
            <div class="form-check" id="checkbox-select-b">
              <input class="form-check-input select" id="input-select-b"
                     name="select" type="checkbox" value="b"/>
              <label class="form-check-label" for="input-select-b">B</label>
            </div>
          </div>
        </div>
        """,
            fxml(widget()),
        )

    def test_checkbox_renders_form_check_input(self):
        widget = factory('#field:checkbox', name='checkbox', props={'label': 'Checkbox'})
        self.checkOutput(
            """
        <div class="form-group" id="field-checkbox">
          <label for="input-checkbox">Checkbox</label>
          <input class="form-check-input" id="input-checkbox" name="checkbox"
                 type="checkbox" value=""/>
          <input id="checkboxexists-checkbox" name="checkbox-exists"
                 type="hidden" value="checkboxexists"/>
        </div>
        """,
            fxml(widget()),
        )

    def test_file_renders_form_control_file(self):
        widget = factory('#field:file', name='file', props={'label': 'File'})
        self.checkOutput(
            """
        <div class="form-group" id="field-file">
          <label for="input-file">File</label>
          <input class="form-control-file" id="input-file" name="file"
                 type="file"/>
        </div>
        """,
            fxml(widget()),
        )

    def test_button_macro_renders_primary_button(self):
        widget = factory('#button', name='button', props={'text': 'Button'})
        self.checkOutput(
            """
        <button class="btn btn-primary" id="input-button" name="action.button"
                type="submit">Button</button>
        """,
            fxml(widget()),
        )

    def test_form_macro_renders_form_without_class(self):
        widget = factory('#form', name='form', props={'action': 'action'})
        self.checkOutput(
            """
        <form action="action" enctype="multipart/form-data" id="form-form"
              method="post" novalidate="novalidate"/>
        """,
            fxml(widget()),
        )

    def test_arrayfield_macro_renders_form_group(self):
        widget = factory(
            '#arrayfield:text', name='text', props={'label': 'Text', 'help': 'Help'}
        )
        self.checkOutput(
            """
        <div class="form-group" id="field-text">
          <label for="input-text">Text</label>
          <input class="form-control" id="input-text" name="text" type="text"
                 value=""/>
          <small class="form-text text-muted">Help</small>
        </div>
        """,
            fxml(widget()),
        )

    def test_array_macro_places_array_in_columns(self):
        # yafowil.widget.array is no dependency, hence check registration
        self.assertEqual(
            factory._macros['array'],
            (
                ['field', 'label', 'help', 'error', 'array'],
                {
                    'array.label': ' ',
                    'label.class_add': 'col-sm-2',
                    'array.class_add': 'col-sm-10',
                    'help.class_add': 'offset-sm-2 col-sm-10',
                    'error.class_add': 'offset-sm-2 col-sm-10',
                },
            ),
        )


class TestBootstrap5(BootstrapTestCase):
    def setUp(self):
        super(TestBootstrap5, self).setUp()
        configure_factory('bootstrap5')

    def test_text_field_renders_field_with_form_label(self):
        self.checkOutput(
            """
        <div class="field mb-2" id="field-text">
          <label class="form-label required" for="input-text">Text</label>
          <input class="form-control required" id="input-text" name="text"
                 required="required" type="text" value=""/>
          <div class="form-text">Help</div>
        </div>
        """,
            fxml(text_field()()),
        )

    def test_text_field_with_error_renders_invalid_feedback(self):
        widget = text_field()
        data = widget.extract({'text': ''})
        self.checkOutput(
            """
        <div class="field mb-2" id="field-text">
          <label class="form-label required" for="input-text">Text</label>
          <input class="form-control is-invalid required" id="input-text"
                 name="text" required="required" type="text" value=""/>
          <div class="invalid-feedback">Required</div>
          <div class="form-text">Help</div>
        </div>
        """,
            fxml(widget(data=data)),
        )

    def test_text_field_with_valid_value_renders_is_valid(self):
        widget = text_field()
        data = widget.extract({'text': 'value'})
        self.checkOutput(
            """
        <div class="field mb-2" id="field-text">
          <label class="form-label required" for="input-text">Text</label>
          <input class="form-control is-valid required" id="input-text"
                 name="text" required="required" type="text" value="value"/>
          <div class="form-text">Help</div>
        </div>
        """,
            fxml(widget(data=data)),
        )

    def test_text_field_in_display_mode_renders_disabled_form_control(self):
        widget = factory(
            '#field:text',
            name='text',
            value='value',
            mode='display',
            props={'label': 'Text'},
        )
        self.checkOutput(
            """
        <div class="field mb-2" id="field-text">
          <label class="form-label">Text</label>
          <div class="form-control disabled text-muted display-form-control"
               id="display-text">value</div>
        </div>
        """,
            fxml(widget()),
        )

    def test_select_renders_form_select(self):
        self.checkOutput(
            """
        <div class="field mb-2" id="field-select">
          <label class="form-label" for="input-select">Select</label>
          <select class="form-select select" id="input-select" name="select">
            <option id="input-select-a" value="a">A</option>
            <option id="input-select-b" value="b">B</option>
          </select>
        </div>
        """,
            fxml(select_field()()),
        )

    def test_select_in_display_mode_renders_disabled_list_group(self):
        widget = factory(
            '#field:select',
            name='select',
            value=['a'],
            mode='display',
            props={
                'label': 'Select',
                'vocabulary': [('a', 'A'), ('b', 'B')],
                'multivalued': True,
            },
        )
        self.checkOutput(
            """
        <div class="field mb-2" id="field-select">
          <label class="form-label">Select</label>
          <ul class="list-group disabled display-select" id="display-select">
            <li class="list-group-item disabled">A</li>
          </ul>
        </div>
        """,
            fxml(widget()),
        )

    def test_single_listing_select_renders_form_check_radios(self):
        self.checkOutput(
            """
        <div class="field mb-2" id="field-select">
          <label class="form-label" for="input-select">Select</label>
          <input id="exists-select" name="select-exists" type="hidden"
                 value="exists"/>
          <div id="radio-select-wrapper">
            <div class="form-check" id="radio-select-a">
              <input class="form-check-input select" id="input-select-a"
                     name="select" type="radio" value="a"/>
              <label class="form-check-label" for="input-select-a">A</label>
            </div>
            <div class="form-check" id="radio-select-b">
              <input class="form-check-input select" id="input-select-b"
                     name="select" type="radio" value="b"/>
              <label class="form-check-label" for="input-select-b">B</label>
            </div>
          </div>
        </div>
        """,
            fxml(select_field(format='single')()),
        )

    def test_multivalued_listing_select_renders_form_check_checkboxes(self):
        widget = select_field(format='single', multivalued=True)
        self.checkOutput(
            """
        <div class="field mb-2" id="field-select">
          <label class="form-label" for="input-select">Select</label>
          <input id="exists-select" name="select-exists" type="hidden"
                 value="exists"/>
          <div id="checkbox-select-wrapper">
            <div class="form-check" id="checkbox-select-a">
              <input class="form-check-input select" id="input-select-a"
                     name="select" type="checkbox" value="a"/>
              <label class="form-check-label" for="input-select-a">A</label>
            </div>
            <div class="form-check" id="checkbox-select-b">
              <input class="form-check-input select" id="input-select-b"
                     name="select" type="checkbox" value="b"/>
              <label class="form-check-label" for="input-select-b">B</label>
            </div>
          </div>
        </div>
        """,
            fxml(widget()),
        )

    def test_checkbox_renders_form_check_input(self):
        widget = factory('#field:checkbox', name='checkbox', props={'label': 'Checkbox'})
        self.checkOutput(
            """
        <div class="field mb-2" id="field-checkbox">
          <label class="form-label" for="input-checkbox">Checkbox</label>
          <input class="form-check-input" id="input-checkbox" name="checkbox"
                 type="checkbox" value=""/>
          <input id="checkboxexists-checkbox" name="checkbox-exists"
                 type="hidden" value="checkboxexists"/>
        </div>
        """,
            fxml(widget()),
        )

    def test_file_renders_form_control(self):
        widget = factory('#field:file', name='file', props={'label': 'File'})
        self.checkOutput(
            """
        <div class="field mb-2" id="field-file">
          <label class="form-label" for="input-file">File</label>
          <input class="form-control mb-2" id="input-file" name="file"
                 type="file"/>
        </div>
        """,
            fxml(widget()),
        )

    def test_button_macro_renders_primary_submit_button(self):
        widget = factory('#button', name='button', props={'label': 'Button'})
        self.checkOutput(
            """
        <input class="btn btn-primary my-3" id="input-button"
               name="action.button" type="submit" value="Button"/>
        """,
            fxml(widget()),
        )

    def test_form_macro_renders_form_without_class(self):
        widget = factory('#form', name='form', props={'action': 'action'})
        self.checkOutput(
            """
        <form action="action" enctype="multipart/form-data" id="form-form"
              method="post" novalidate="novalidate"/>
        """,
            fxml(widget()),
        )

    def test_arrayfield_macro_renders_field(self):
        widget = factory(
            '#arrayfield:text', name='text', props={'label': 'Text', 'help': 'Help'}
        )
        self.checkOutput(
            """
        <div class="field mb-2" id="field-text">
          <label class="form-label" for="input-text">Text</label>
          <input class="form-control" id="input-text" name="text" type="text"
                 value=""/>
          <div class="form-text">Help</div>
        </div>
        """,
            fxml(widget()),
        )

    def test_array_macro_aligns_array_to_the_end(self):
        # yafowil.widget.array is no dependency, hence check registration
        self.assertEqual(
            factory._macros['array'],
            (
                ['field', 'label', 'help', 'error', 'array'],
                {
                    'array.label': ' ',
                    'label.class_add': '',
                    'array.class_add': 'd-flex justify-content-end',
                    'help.class_add': '',
                    'error.class_add': 'd-flex justify-content-end',
                },
            ),
        )

    def test_color_placement_property_is_documented(self):
        self.assertIn('popper.js', factory.doc['props']['color.placement'])
