httpie-api-auth
===============

`ApiAuth <https://github.com/mgomes/api_auth>`_ auth plugin for `HTTPie <https://github.com/jkbr/httpie>`_.

Installation
------------

.. code-block:: bash

    $ pip install httpie-api-auth

You should now see ``api-auth`` under ``--auth-type`` in ``$ http --help`` output.

Usage
-----

.. code-block:: bash

    $ http --auth-type=api-auth --auth='access_id:secret_key' example.org
