from yafowil.base import factory
from yafowil.compound import (
    hybrid_extractor,
    div_renderer,
)


factory.register(
    'bs_controls',
    extractors=[hybrid_extractor],
    edit_renderers=[div_renderer],
    display_renderers=[div_renderer])


BOOTSTRAP_MACROS = {
    'form': {
        'chain': 'form',
        'props': {
            'form.class': 'form-horizontal',
        }
    },
    'field': {
        'chain': 'field:label:bs_controls',
        'props': {
            'field.class': 'control-group',
            'label.class': 'control-label',
            'bs_controls.class': 'controls',
        }
    },
    'button': {
        'chain': 'submit',
        'props': {
            'submit.class': 'btn btn-primary',
        }
    },
}

for name, value in BOOTSTRAP_MACROS.items():
    factory.register_macro(name, value['chain'], value['props'])
