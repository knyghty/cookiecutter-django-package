===========================
cookiecutter-django-package
===========================

A minimalist Cookiecutter template for creating a Django reusable app.

The aim is to to the boring stuff you need for almost every package,
without making any assumptions about what you're building.


Usage
=====

1. `Install Cookiecutter`_.
2. Run ``cookiecutter gh:knyghty/cookiecutter-django-package``.

What this does
==============

This template has an opinionated setup. It includes the following:

* ``pyproject.toml`` for configuration.
* A GitHub actions workflow that:
  * Runs the test across supported Python and Django versions.
  * Publishes to PyPI using Trusted Publisher Management.
* Ruff for linting and formatting, with pre-commit configuration.
* A working test setup.
* An empty Django app.
* dependabot configuration for updating GitHub Actions.

What this doesn't do
====================

* It's assumed you'll run pre-commit CI, so linting isn't run through GitHub Actions.
* The linting configuration is quite minimal, you may want to add more `Ruff rules`_.
* There's no documentation. Most projects can get away with a README until they grow.
* However, I'd welcome a PR adding optional Sphinx / readthedocs support.
* There's no changelog or version management support. I just change the version in
  ``pyproject.toml`` and commit it and make a GitHub release using their generated
  release notes, which is good enough for me.
* There isn't (yet) much configuration, if for example you want to use a different
  license or test on multiple databases. While this is a minimalist template I made
  for my own projects, I would welcome PRs for more (useful) configuration options.

Notes
=====

You only need the ``apps.py`` if you're adding models, templates, static, template tags,
or something else that Django needs in an app for auto-discovery. If you don't do
any of these things, it can be removed, and it should also be removed from
``INSTALLED_APPS`` in ``tests/settings.py``.

.. _Install Cookiecutter: https://cookiecutter.readthedocs.io/en/stable/installation.html
.. _Ruff rules: https://docs.astral.sh/ruff/rules/
