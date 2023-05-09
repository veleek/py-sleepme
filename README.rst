========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |github-actions|
        | |codecov|
        | |scrutinizer|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/py-sleepme/badge/?style=flat
    :target: https://py-sleepme.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/veleek/py-sleepme/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/veleek/py-sleepme/actions

.. |codecov| image:: https://codecov.io/gh/veleek/py-sleepme/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://app.codecov.io/github/veleek/py-sleepme

.. |version| image:: https://img.shields.io/pypi/v/sleepme.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/sleepme

.. |wheel| image:: https://img.shields.io/pypi/wheel/sleepme.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/sleepme

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/sleepme.svg
    :alt: Supported versions
    :target: https://pypi.org/project/sleepme

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/sleepme.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/sleepme

.. |commits-since| image:: https://img.shields.io/github/commits-since/veleek/py-sleepme/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/veleek/py-sleepme/compare/v0.0.1...main


.. |scrutinizer| image:: https://img.shields.io/scrutinizer/quality/g/veleek/py-sleepme/main.svg
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/veleek/py-sleepme/


.. end-badges

A python library for the Sleep.me Developer API.

* Free software: MIT license

Installation
============

::

    pip install sleepme

You can also install the in-development version with::

    pip install https://github.com/veleek/py-sleepme/archive/main.zip


Documentation
=============


https://py-sleepme.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
