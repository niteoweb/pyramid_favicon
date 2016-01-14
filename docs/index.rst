===================
``pyramid_favicon``
===================

Overview
========

``pyramid_favicon`` is an add-on for handling favicons in your Pyramid project. 
Normally, the favicon.ico file is stored on a web site's project root 
(e.g. /myproject_root/favicon.ico). However, with this add-on, it is possible 
to specify a different location of favicon.ico via a custom config setting 
(e.g. /myproject_root/some/other/location/favicon.ico).

Installation
============

Install using setuptools, e.g. (within a virtualenv)::

  $ $myenv/bin/easy_install pyramid_favicon

Setup
=====

After installing ``pyramid_favicon`` into your environment, you will need
to activate it in your project using one of the following methods:

#) Add ``pyramid_favicon`` in the `pyramid.includes` section of your
   project's ``.ini`` file:

.. code-block:: ini
   :linenos:

   [app:myapp]
   pyramid.includes = pyramid_favicon

#) Alternately, include ``pyramid_favicon`` using the ``confic.include``
   directive in your Pyramid project configuration. That is, inside
   ``__init__.py``, include the following lines:

.. code-block:: python
   :linenos:

   config = Configurator(.....)
   config.include('pyramid_favicon')

Reporting Bugs / Development Versions
=====================================

Visit http://github.com/niteoweb/pyramid_favicon to download development or 
tagged versions.

Visit http://github.com/niteoweb/pyramid_favicon/issues to report bugs.

