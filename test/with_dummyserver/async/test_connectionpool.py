from threading import Event

import pytest

from ahip import HTTPConnectionPool
from ahip.exceptions import ReadTimeoutError

from dummyserver.testcase import SocketDummyServerTestCase
from test import SHORT_TIMEOUT, LONG_TIMEOUT
from test.with_dummyserver import conftest


def wait_for_socket(ready_event):
    ready_event.wait()
    ready_event.clear()


class TestConnectionPoolTimeouts(SocketDummyServerTestCase):
    @conftest.test_all_backends
    async def test_timeout_float(self, backend, anyio_backend):
        block_event = Event()
        ready_event = self.start_basic_handler(block_send=block_event, num=2)

        with HTTPConnectionPool(
            self.host, self.port, backend=backend, retries=False
        ) as pool:
            wait_for_socket(ready_event)
            with pytest.raises(ReadTimeoutError):
                await pool.request("GET", "/", timeout=SHORT_TIMEOUT)
            block_event.set()  # Release block

            # Shouldn't raise this time
            wait_for_socket(ready_event)
            block_event.set()  # Pre-release block
            await pool.request("GET", "/", timeout=LONG_TIMEOUT)
