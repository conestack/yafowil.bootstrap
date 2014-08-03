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
    #factory.defaults['label.help'] = None

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
        'table table-bordered table-condensed'

    # yafowil.widget.dict
    factory.defaults['dict.table_class'] = \
        'dictwidget table table-bordered table-condensed'

    # yafowil.widget.datetime
    factory.defaults['datetime.datepicker_class'] = 'datepicker input-medium'
    factory.defaults['datetime.timepicker_class'] = 'timepicker input-small'

    # yafowil.widget.wysihtml5
    factory.defaults['wysihtml5.class'] = 'wysihtml5 form-control'


def register_macros():
    macros = {
        'form': {
            'chain': 'form',
            'props': {
                'form.class': 'form-horizontal',
            }
        },
        'field': {
            'chain': 'field:label:div:help:error',
            'props': {
                'label.class_add': 'col-sm-2',
                'div.class_add': 'col-sm-10',
            }
        },
        'button': {
            'chain': 'submit',
            'props': {
                'submit.class': 'btn',
                'submit.class_add': 'btn-default',
            }
        },
    }
    for name, value in macros.items():
        factory.register_macro(name, value['chain'], value['props'])
