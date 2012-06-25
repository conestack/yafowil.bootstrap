from yafowil.base import factory
from yafowil.compound import (
    hybrid_extractor,
    div_renderer,
)

factory.theme = 'bootstrap'

factory.register(
    'bs_controls',
    extractors=[hybrid_extractor],
    edit_renderers=[div_renderer],
    display_renderers=[div_renderer])


def bs_field_error_class(widget, data):
    if data.errors:
        return 'error'
    return ''


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
            'field.class': 'control-group',
            'field.class_add': bs_field_error_class,
            'label.class': 'control-label',
            'label.help': None,
            'error.position': 'after',
            'error.tag': 'span',
            'error.class': 'help-inline',
            'help.position': 'after',
            'help.tag': 'p',
            'help.class': 'help-block',
            'bs_controls.class': 'controls',
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

factory.defaults['select.label_radio_class'] = 'radio'
factory.defaults['select.label_checkbox_class'] = 'checkbox'
