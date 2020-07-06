from yafowil.base import factory
from yafowil.utils import attr_value


def configure_factory():
    # set theme
    factory.theme = "bootstrap4"

    # wrapper div for one input
    factory.defaults["field.class"] = "form-group"

    # label required marker (plone)
    factory.defaults["label.required_class"] = "required"

    # common defaults
    # form-control:
    # errors: https://getbootstrap.com/docs/4.4/components/forms/#how-it-works
    bs4_input_blueprints = [
        "text", "textarea", "lines", "password", "email", "url", "search"
    ]
    for blueprint_name in bs4_input_blueprints:
        factory.defaults["{0}.class".format(blueprint_name)] = "form-control"
        factory.defaults["{0}.error_class".format(blueprint_name)] = "is-invalid"
        factory.defaults["{0}.valid_class".format(blueprint_name)] = "is-valid"


    factory.defaults["submit.class"] = "btn btn-primary"
    factory.defaults["button.class"] = "btn btn-primary"

    factory.defaults["error.position"] = "after"
    factory.defaults["error.tag"] = "div"
    factory.defaults["error.class"] = "invalid-feedback"
    factory.defaults["error.message_class"] = None
    factory.defaults['error.message_tag'] = None

    factory.defaults["help.position"] = "after"
    factory.defaults["help.tag"] = "small"
    factory.defaults["help.class"] = "form-text text-muted"

    # select
    factory.defaults["select.block_class"] = "form-control"
    factory.defaults["select.radio_input_class"] = "form-check-input"
    factory.defaults["select.radio_label_class"] = "form-check-label"
    factory.defaults["select.radio_wrapper_class"] = "form-check"
    factory.defaults["select.checkbox_input_class"] = "form-check-input"
    factory.defaults["select.checkbox_label_class"] = "form-check-label"
    factory.defaults["select.checkbox_wrapper_class"] = "form-check"
    factory.defaults["select.listing_label_position"] = "after"

    # single checkbox
    factory.defaults["checkbox.class"] = "form-check-input"

    # yafowil.widget.array
    factory.defaults["array.table_class"] = "table table-condensed"

    # yafowil.widget.autocomplete
    factory.defaults["autocomplete.class"] = "autocomplete form-control"

    # yafowil.widget.chosen
    factory.defaults["chosen.class"] = "chosen form-control"

    # yafowil.widget.datetime
    factory.defaults["datetime.datepicker_class"] = "datepicker form-control"
    factory.defaults["datetime.timepicker_class"] = "timepicker form-control"
    factory.defaults["time.timepicker_class"] = "timepicker form-control"

    # yafowil.widget.dict
    factory.defaults["dict.table_class"] = "dictwidget table table-condensed"
    factory.defaults["dict.key_class"] = "form-control"
    factory.defaults["dict.value_class"] = "form-control"

    # yafowil.widget.wysihtml5
    factory.defaults["wysihtml5.class"] = "wysihtml5 form-control"


def register_macros():
    # common
    factory.register_macro("form", "form", {})

    factory.register_macro("field", "field:label:help:error", {})

    factory.register_macro(
        "button", "button", {"button.class": "btn", "button.class_add": "btn-primary",},
    )

    # yafowil.widget.array
    factory.register_macro(
        "array",
        "field:label:help:error:array",
        {
            "array.label": " ",
            "label.class_add": "col-sm-2",
            "array.class_add": "col-sm-10",
            "help.class_add": "col-sm-offset-2 col-sm-10",
            "error.class_add": "col-sm-offset-2 col-sm-10",
        },
    )
    factory.register_macro("arrayfield", "field:label:help:error", {})
