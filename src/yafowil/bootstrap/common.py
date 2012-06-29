from yafowil.base import factory


factory.theme = 'bootstrap'
factory.defaults['select.label_radio_class'] = 'radio'
factory.defaults['select.label_checkbox_class'] = 'checkbox'

# yafowil.widget.array
factory.defaults['array.table_class'] = 'table table-bordered table-condensed'

# yafowil.widget.dict
factory.defaults['dict.table_class'] = 'dictwidget table table-bordered ' +\
                                       'table-condensed'

# yafowil.widget.datetime
factory.defaults['datetime.datepicker_class'] = 'datepicker input-medium'
factory.defaults['datetime.timepicker_class'] = 'timepicker input-small'

def bs_controls_renderer(widget, data):
    return data.tag('div', data.rendered, class_='controls')

factory.register(
    'bs_controls',
    extractors=[],
    edit_renderers=[bs_controls_renderer],
    display_renderers=[bs_controls_renderer])


def bs_field_class(widget, data):
    if data.errors:
        return 'control-group error'
    return 'control-group'

BOOTSTRAP_MACROS = {
    'form': {
        'chain': 'form',
        'props': {
            'form.class': 'form-horizontal',
        }
    },
    'field': {
        'chain': 'field:label:bs_controls:help:error',
        'props': {
            'field.class': bs_field_class,
            'label.class': 'control-label',
            'label.help': None,
            'error.position': 'after',
            'error.tag': 'span',
            'error.class': 'help-inline',
            'help.position': 'after',
            'help.tag': 'p',
            'help.class': 'help-block',
        }
    },
    'button': {
        'chain': 'submit',
        'props': {
            'submit.class': 'btn',
        }
    },
}

for name, value in BOOTSTRAP_MACROS.items():
    factory.register_macro(name, value['chain'], value['props'])
