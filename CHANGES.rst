Changes
=======

2.0.0 (unreleased)
------------------

- Add Makefile.
  [lenadax]

- Configure tests to run with pytest.
  [lenadax]


2.0.0a2 (2024-04-30)
--------------------

- Update BS4 resources to latest 4.6.2
  [petschki]

- Update BS5 resources to latest 5.3.3
  [petschki]

- Fix CSS class for <select>.
  [petschki]


2.0.0a1 (2023-05-15)
--------------------

- Factory configuration and macro registration is no longer done automatically
  due to the multi-theme feature. It must be configured in your code using
  ``yafowil.bootstrap``. In order to do so do
  ``from yafowil.bootstrap import configure_factory``. Next call it with the
  name of the desired theme ``configure_factory('bootstrap3')``.
  [jensens]

- Add support for Bootstrap 4 and 5 using theme ``bootstrap[4|5]``.
  The Bootstrap 3 theme is still available as ``bootstrap3``.
  Latter provides a legacy fallback as ``bootstrap`` which will be removed in
  future versions.
  [jensens, agitator]


1.3.2 (2022-12-05)
------------------

- Release wheel.
  [rnix]

- Remove empty doctest.
  [rnix]


1.3.1 (2017-11-13)
------------------

- Use ``bs_field_class`` callback for ``field.class`` property when registering
  ``array`` macro.
  [rnix]


1.3 (2017-03-01)
----------------

- Use ``yafowil.utils.entry_point`` decorator.
  [rnix]

- Cleanup macro registration.
  [rnix]


1.2 (2015-01-23)
----------------

- Use ``configure`` entry point for theme configuration.
  [rnix]

- Rename resource group ``bootstrap`` to ``bootstrap.dependencies``.
  [rnix]

- Remove bootstrap macros for yafowil and set factory defaults for common
  widgets where appropriate.
  [rnix]

- Update to bootstrap 3.2.
  [rnix]


1.1
---

- Register the bootstrap.js javascript too.
  [thet]


1.0
---

- make it work
  [rnix, jensens, thet, et al.]
