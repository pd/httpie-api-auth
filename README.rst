httpie-api_auth
===============

`ApiAuth <https://github.com/mgomes/api_auth>`_ auth plugin for `HTTPie <https://github.com/jkbr/httpie>`_.

Installation
------------

.. code-block:: bash

    $ pip install httpie-api_auth

You should now see ``api`` under ``--auth-type`` in ``$ http --help`` output.

Usage
-----

.. code-block:: bash

    $ http --auth-type=api --auth='access_id:secret_key' example.org
