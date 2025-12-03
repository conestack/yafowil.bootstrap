yafowil.bootstrap
=================

.. image:: https://img.shields.io/pypi/v/yafowil.bootstrap.svg
    :target: https://pypi.python.org/pypi/yafowil.bootstrap
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/yafowil.bootstrap.svg
    :target: https://pypi.python.org/pypi/yafowil.bootstrap
    :alt: Number of PyPI downloads

.. image:: https://github.com/conestack/yafowil.bootstrap/actions/workflows/test.yml/badge.svg
    :target: https://github.com/conestack/yafowil.bootstrap/actions/workflows/test.yml
    :alt: Test yafowil.bootstrap

**bootstrap styles integration** for for `YAFOWIL <http://pypi.python.org/pypi/yafowil>`_
- Yet Another Form Widget Library.

This package provides themes for Bootstrap 3, 4 and 5.

In order to select one of the bootstrap versions, ``configure_factory`` must be
called with the desired theme name:

.. code-block:: python

    from yafowil.bootstrap import configure_factory

    # bootstap3, bootstrap4, bootstrap5
    configure_factory('bootstrap5')

Included Bootstrap distributions:

* Bootstrap 3.4.1
* Bootstrap 4.6.0
* Bootstrap 5.1.0

``yafowil.bootstrap`` 2.0 is a transitional version. in 3.0 the bootstrap
distributions will be removed as resource delivery is planned to be changed
to ``webresource``.


Detailed Documentation
======================

If you're interested to dig deeper: The
`detailed YAFOWIL documentation <http://docs.yafowil.info>`_ is available.
Read it and learn how to create your example application with YAFOWIL forms
in 15 minutes.


Source Code
===========

The sources are in a GIT DVCS with its main branches at
`github <http://github.com/conestack/yafowil.bootstrap>`_.

We'd be happy to see many forks and pull-requests to make YAFOWIL even better.


Contributors
============

- Robert Niederrreiter
- Jens Klein
- Johannes Raggam
- Peter Holzer
