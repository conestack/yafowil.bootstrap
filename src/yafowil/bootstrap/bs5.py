from yafowil.base import factory
from yafowil.utils import attr_value


def configure_factory():
    # set theme
    factory.theme = 'bootstrap5'

    # wrapper div for one input
    factory.defaults['field.class'] = 'field'

    # label marker
    factory.defaults['label.class'] = 'form-label'

    # label required marker (plone)
    factory.defaults['label.required_class'] = 'required'

    # common defaults
    # form-control:
    # errors: https://v5.getbootstrap.com/docs/5.0/forms/overview/
    bs5_input_blueprints = [
        'text',
        'textarea',
        'lines',
        'password',
        'email',
        'url',
        'search',
        'number',
        'file',
    ]
    for blueprint_name in bs5_input_blueprints:
        factory.defaults['{0}.class'.format(blueprint_name)] = 'form-control'
        factory.defaults['{0}.error_class'.format(blueprint_name)] = 'is-invalid'
        factory.defaults['{0}.valid_class'.format(blueprint_name)] = 'is-valid'

    factory.defaults['submit.class'] = 'btn btn-primary text-light mb-3'
    factory.defaults['button.class'] = 'btn btn-primary text-light mb-3'

    factory.defaults['error.position'] = 'after'
    factory.defaults['error.tag'] = 'div'
    factory.defaults['error.class'] = 'invalid-feedback'
    factory.defaults['error.message_class'] = None
    factory.defaults['error.message_tag'] = None

    factory.defaults['help.position'] = 'after'
    factory.defaults['help.tag'] = 'div'
    factory.defaults['help.class'] = 'form-text'

    # file
    factory.defaults['file.class'] = 'form-control'

    # select
    factory.defaults['select.error_class'] = 'is-invalid'
    factory.defaults['select.valid_class'] = 'is-valid'
    factory.defaults['select.block_class'] = 'form-control'
    factory.defaults['select.radio_input_class'] = 'form-check-input'
    factory.defaults['select.radio_label_class'] = 'form-check-label'
    factory.defaults['select.radio_wrapper_class'] = 'form-check'
    factory.defaults['select.checkbox_input_class'] = 'form-check-input'
    factory.defaults['select.checkbox_label_class'] = 'form-check-label'
    factory.defaults['select.checkbox_wrapper_class'] = 'form-check'
    factory.defaults['select.listing_label_position'] = 'after'

    # single checkbox
    factory.defaults['checkbox.error_class'] = 'is-invalid'
    factory.defaults['checkbox.valid_class'] = 'is-valid'
    factory.defaults['checkbox.class'] = 'form-check-input'

    # yafowil.widget.ace
    factory.defaults['ace.wrapper_class'] = 'ace-editor-wrapper card'

    # yafowil.widget.array
    factory.defaults['array.table_class'] = 'table table-sm'

    # yafowil.widget.autocomplete
    factory.defaults['autocomplete.class'] = 'autocomplete form-control'

    # yafowil.widget.chosen
    factory.defaults['chosen.class'] = 'chosen form-control'

    # yafowil.widget.color
    factory.defaults['color.block_class'] = 'color form-control'
    factory.defaults['color.placement'] = 'bottom-start'
    factory.doc['props']['color.placement'] = """\
        Specify the color picker dropdown's placement.
        Supply any supported value from the popper.js library.
    """

    # yafowil.widget.datetime
    factory.defaults['datetime.datepicker_class'] = 'datepicker form-control'
    factory.defaults['datetime.timepicker_class'] = 'timepicker form-control'
    factory.defaults['time.timepicker_class'] = 'timepicker form-control'
    factory.defaults['datetime.datepicker_wrapper_class'] = 'input-group'
    factory.defaults['datetime.timepicker_wrapper_class'] = 'input-group'
    factory.defaults['time.timepicker_wrapper_class'] = 'input-group'

    # yafowil.widget.dict
    factory.defaults['dict.table_class'] = 'dictwidget table table-sm'
    factory.defaults['dict.key_class'] = 'form-control'
    factory.defaults['dict.value_class'] = 'form-control'

    # yafowil.widget.wysihtml5
    factory.defaults['wysihtml5.class'] = 'wysihtml5 form-control'

    # yafowil.widget.image
    factory.defaults['image.class'] = 'image form-control mt-3 mb-2'
    factory.defaults['image.radio_class'] = 'form-check'
    factory.defaults['image.radio_input_class'] = 'form-check-input'

    # yafowil.file
    factory.defaults['file.class'] = 'form-control mb-2'
    factory.defaults['file.radio_class'] = 'form-check'
    factory.defaults['file.radio_input_class'] = 'form-check-input'

    # yafowil.widget.cron
    factory.defaults['cron.edit_container_class'] = 'edit-container card'
    factory.defaults['cron.editarea_class'] = 'editarea card-body'
    factory.defaults['cron.options_container_class'] = 'card-header pt-0'
    factory.defaults['cron.options_header_class'] = 'nav nav-tabs card-header-tabs'
    factory.defaults['cron.edit_btn_class'] = 'nav-link edit'


def register_macros():
    # common
    factory.register_macro('form', 'form', {})
    factory.register_macro('field', 'field:label:help:error', {})
    factory.register_macro(
        'button',
        'submit',
        {
            'button.class': 'btn',
            'button.class_add': 'btn-primary my-3',
            'submit.class': 'btn',
            'submit.class_add': 'btn-primary my-3'
        }
    )

    # yafowil.widget.array
    factory.register_macro(
        'array',
        'field:label:help:error:array',
        {
            'array.label': ' ',
            'label.class_add': '',
            'array.class_add': 'd-flex justify-content-end',
            'help.class_add': '',
            'error.class_add': 'd-flex justify-content-end'
        }
    )
    factory.register_macro('arrayfield', 'field:label:help:error', {})
