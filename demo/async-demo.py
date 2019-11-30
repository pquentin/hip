# This should work on python 3.6+

import urllib3
from urllib3.backends import Backend

URL = "http://httpbin.org/uuid"

async def main(backend=None):
    with urllib3.AsyncPoolManager(backend=backend) as http:
        print("URL:", URL)
        r = await http.request("GET", URL, preload_content=False)
        print("Status:", r.status)
        print("Data:", await r.read())

print("--- urllib3 using Trio ---")
import trio
trio.run(main)

print("\n--- urllib3 using asyncio (via AnyIO) ---")
import asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

print("\n--- urllib3 using curio (via AnyIO) ---")
import curio
curio.run(main)

print("\n--- urllib3 using Twisted ---")
from twisted.internet.task import react
from twisted.internet.defer import ensureDeferred
def twisted_main(reactor):
    return ensureDeferred(main(Backend("twisted", reactor=reactor)))
react(twisted_main)
