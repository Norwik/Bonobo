.. image:: https://img.shields.io/pypi/v/pinkman.svg
    :alt: PyPI-Server
    :target: https://pypi.org/project/pinkman/
.. image:: https://github.com/clivern/pinkman/actions/workflows/ci.yml/badge.svg
    :alt: Build Status
    :target: https://github.com/clivern/pinkman/actions/workflows/ci.yml

|

=======
Pinkman
=======

To use pinkman, follow the following steps:

1. Create a python virtual environment or use system wide environment

.. code-block::

    $ python3 -m venv venv
    $ source venv/bin/activate


2. Install pinkman package with pip.

.. code-block::

    $ pip install pinkman


3. Create the config file.

.. code-block::

    server:
      hostname: localhost
      port: 1025

    cache:
      type: sqlite
      path: /tmp/pinkman.db

    backend:
      type: http
      method: post
      url: https://pinkman.free.beeceptor.com
      apikey: 5ab99869-f403-4481-bed6-da7c8aad7521


4. Run the pinkman server.

.. code-block::

    $ pinkman server run -c /etc/config.prod.yml


5. Run the pinkman worker.

.. code-block::

    $ pinkman worker run -c /etc/config.prod.yml
