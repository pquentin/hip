from ahip import HTTPConnectionPool

from dummyserver.testcase import SocketDummyServerTestCase
from test.with_dummyserver import conftest


class TestCookies(SocketDummyServerTestCase):
    @conftest.test_all_backends
    async def test_multi_setcookie(self, backend, anyio_backend):
        def multicookie_response_handler(listener):
            sock = listener.accept()[0]

            buf = b""
            while not buf.endswith(b"\r\n\r\n"):
                buf += sock.recv(65536)

            sock.send(
                b"HTTP/1.1 200 OK\r\n"
                b"Set-Cookie: foo=1\r\n"
                b"Set-Cookie: bar=1\r\n"
                b"\r\n"
            )
            sock.close()

        self._start_server(multicookie_response_handler)
        with HTTPConnectionPool(self.host, self.port, backend=backend) as pool:
            r = await pool.request("GET", "/", retries=0)
            assert r.headers == {"set-cookie": "foo=1, bar=1"}
            assert r.headers.getlist("set-cookie") == ["foo=1", "bar=1"]
