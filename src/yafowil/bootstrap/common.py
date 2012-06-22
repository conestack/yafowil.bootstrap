from yafowil.base import factory
from yafowil.compound import (
    hybrid_extractor,
    compound_renderer,
    div_renderer,
)
from yafowil.utils import (
    cssclasses,
    css_managed_props,
    managedprops,
)


@managedprops('id', *css_managed_props)
def bs_controls_renderer(widget, data):
    attrs = {
        'id': widget.attrs.get('id'),
        'class_': cssclasses(widget, data),
    }
    if len(widget):
        rendered = compound_renderer(widget, data)
    else:
        rendered = data.rendered
    if data.errors:
        msgs = [error.message for error in data.errors]
        rendered += data.tag('span', ', '.join(msgs), class_='help-inline')
    if widget.attrs['help']:
        rendered += data.tag('p', widget.attrs['help'], class_='help-block')
    return data.tag('div', rendered, **attrs)


factory.register(
    'bs_controls',
    extractors=[hybrid_extractor],
    edit_renderers=[bs_controls_renderer],
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
        'chain': 'field:label:bs_controls',
        'props': {
            'field.class': 'control-group',
            'field.class_add': bs_field_error_class,
            'label.class': 'control-label',
            'bs_controls.class': 'controls',
            'bs_controls.help': None,
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
