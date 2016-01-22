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

Compatibility
-------------

As of version 0.3.0 of this library, only the new canonical string form introduced in
`api_auth 1.4 <https://github.com/mgomes/api_auth/blob/master/CHANGELOG.md#14-2015-12-16>`_ is
supported. If you need to interact with services that have not yet upgraded to be compatible
with this new scheme, you will need to use version 0.2.1 of this library to sign requests
in a manner that those services will accept.
