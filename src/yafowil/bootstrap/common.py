from yafowil.base import factory


def bs_field_class(widget, data):
    if data.errors:
        return 'form-group has-error'
    return 'form-group'


def configure_factory():
    # set theme
    factory.theme = 'bootstrap'

    # common defaults
    factory.defaults['text.class'] = 'text form-control'

    factory.defaults['textarea.class'] = 'textarea form-control'

    factory.defaults['lines.class'] = 'lines form-control'

    factory.defaults['password.class'] = 'password form-control'

    factory.defaults['select.class'] = 'select'
    factory.defaults['select.block_class'] = 'form-control'
    factory.defaults['select.radio_wrapper_class'] = 'radio'
    factory.defaults['select.checkbox_wrapper_class'] = 'checkbox'

    factory.defaults['submit.class'] = 'btn btn-default'

    factory.defaults['email.class'] = 'email form-control'

    factory.defaults['url.class'] = 'url form-control'

    factory.defaults['search.class'] = 'search form-control'

    factory.defaults['number.class'] = 'number form-control'

    factory.defaults['label.class'] = 'control-label'

    factory.defaults['field.class'] = bs_field_class

    factory.defaults['error.position'] = 'after'
    factory.defaults['error.tag'] = 'span'
    factory.defaults['error.class'] = 'help-block'
    factory.defaults['error.message_class'] = 'text-danger'

    factory.defaults['help.position'] = 'after'
    factory.defaults['help.tag'] = 'p'
    factory.defaults['help.class'] = 'help-block'

    # yafowil.widget.array
    factory.defaults['array.table_class'] = \
        'table table-condensed'

    # yafowil.widget.autocomplete
    factory.defaults['autocomplete.class'] = 'autocomplete form-control'

    # yafowil.widget.chosen
    factory.defaults['chosen.class'] = 'chosen form-control'

    # yafowil.widget.datetime
    factory.defaults['datetime.datepicker_class'] = 'datepicker form-control'
    factory.defaults['datetime.timepicker_class'] = 'timepicker form-control'
    factory.defaults['time.timepicker_class'] = 'timepicker form-control'

    # yafowil.widget.dict
    factory.defaults['dict.table_class'] = \
        'dictwidget table table-condensed'
    factory.defaults['dict.key_class'] = 'form-control'
    factory.defaults['dict.value_class'] = 'form-control'

    # yafowil.widget.wysihtml5
    factory.defaults['wysihtml5.class'] = 'wysihtml5 form-control'


def register_macros():
    # common
    factory.register_macro('form', 'form', {
        'form.class': 'form-horizontal',
    })
    factory.register_macro('field', 'field:label:div:help:error', {
        'label.class_add': 'col-sm-2',
        'div.class_add': 'col-sm-10',
    })
    factory.register_macro('button', 'submit', {
        'submit.class': 'btn',
        'submit.class_add': 'btn-default',
    })

    # yafowil.widget.array
    factory.register_macro('array', 'field:label:help:error:array', {
        'array.label': ' ',
        'field.class': bs_field_class,
        'label.class_add': 'col-sm-2',
        'array.class_add': 'col-sm-10',
        'help.class_add': 'col-sm-offset-2 col-sm-10',
        'error.class_add': 'col-sm-offset-2 col-sm-10',
    })
    factory.register_macro('arrayfield', 'field:label:help:error', {})
