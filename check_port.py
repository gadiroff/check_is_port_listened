#!/usr/bin/python
import time
import asyncio

host = "8.8.8.8"
port = 53
duration = 10
delay = 2
timeout = 5

async def wait_host_port(host, port, duration, delay, timeout):

    tmax = time.time() + duration
    while time.time() < tmax:
        try:
            writer = await asyncio.wait_for(asyncio.open_connection(host, port), timeout)
            writer.close()
            await writer.wait_closed()
            return True
        except:
            if delay:
                await asyncio.sleep(delay)
    return False

print(asyncio.run(wait_host_port(host, port, duration, delay, timeout)))
