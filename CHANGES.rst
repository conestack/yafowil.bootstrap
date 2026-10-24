Changes
=======

2.0.1 (unreleased)
------------------

- Fix the bootstrap 4 ``array`` macro using the bootstrap 3 grid class
  ``col-sm-offset-2`` for help and error, it is ``offset-sm-2`` in bootstrap 4.
  [rnix]

- Remove settings without effect: the bootstrap 5 ``file.class`` default
  overwritten later in ``configure_factory`` and the ``button.class`` props of
  the bootstrap 5 ``button`` macro, which renders a ``submit`` blueprint.
  [rnix]

- Modernise the code ruff flags as outdated: ``.format()`` over f-strings.
  Behaviour unchanged. ``super(Class, self)`` is kept, see ``cone.app``.
  [rnix]

- Sort the imports with ruff (one per line, ``from`` imports first, no
  sections) and format the code with ``ruff format`` (90 characters per line,
  single quotes).
  [rnix]

- Add ``qa.ruff`` domain to Makefile and pin the ruff configuration in
  ``pyproject.toml``, ``make check`` runs ``ruff check``.
  [rnix]


2.0.0 (2026-02-03)
------------------

- Refactor package layout to use ``pyproject.toml`` and implicit namespace packages.
  [rnix]

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


1.3.3 (2025-10-28)
------------------

- Pin upper versions of dependencies.
  [rnix]


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
