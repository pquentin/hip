hip
===

.. image:: https://travis-ci.org/python-trio/hip.svg?branch=master
        :alt: Build status on Travis
        :target: https://travis-ci.org/python-trio/hip

.. image:: https://github.com/python-trio/hip/workflows/CI/badge.svg
        :alt: Build status on GitHub Actions
        :target: https://github.com/python-trio/hip/actions

.. image:: https://img.shields.io/codecov/c/github/python-trio/hip.svg
        :alt: Coverage Status
        :target: https://codecov.io/gh/python-trio/hip

.. image:: https://img.shields.io/pypi/v/hip.svg?maxAge=86400
        :alt: PyPI version
        :target: https://pypi.org/project/hip/

.. image:: https://badges.gitter.im/python-trio/hip.svg
        :alt: Gitter
        :target: https://gitter.im/python-trio/hip

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

hip is a new Python HTTP client for everybody. It supports synchronous Python (just like requests does), but also Trio, asyncio and Curio.

hip is robust as it is based on urllib3 and uses its extensive test suite that was refined over the years. I also shares most urllib3 features:

- Thread safety.
- Connection pooling.
- Client-side SSL/TLS verification.
- File uploads with multipart encoding.
- Helpers for retrying requests and dealing with HTTP redirects.
- Support for gzip, deflate, and brotli encoding.
- Proxy support for HTTP.
- 100% test coverage.

However, we currently do not support SOCKS proxies nor the pyOpenSSL and SecureTransport TLS backends.

Sample code
-----------

hip is powerful and easy to use::

    >>> import hip
    >>> http = hip.PoolManager()
    >>> r = http.request('GET', 'http://httpbin.org/robots.txt')
    >>> r.status
    200
    >>> r.data
    'User-agent: *\nDisallow: /deny\n'

It also supports async/await::

    import hip
    import trio

    async def main():
        with hip.AsyncPoolManager() as http:
            r = await http.request("GET", "http://httpbin.org/uuid")
            print("Status:", r.status)  # 200
            print("Data:", await r.read()). # 'User-agent: *\nDisallow: /deny\n'

    trio.run(main)

Installing
----------

hip can be installed with `pip <https://pip.pypa.io>`_::

    $ pip install hip

Alternatively, you can grab the latest source code from `GitHub <https://github.com/python-trio/hip>`_::

    $ git clone git://github.com/python-trio/hip.git
    $ python setup.py install


Documentation
-------------

hip will soon have usage and reference documentation at `hip.readthedocs.io <https://hip.readthedocs.io/en/latest/>`_.


Contributing
------------

hip happily accepts contributions. Please see our
`contributing documentation <https://hip.readthedocs.io/en/latest/contributing.html>`_
for some tips on getting started.
