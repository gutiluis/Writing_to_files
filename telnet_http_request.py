#!/usr/bin/env python3

# script to test server with log in same working directory
# check with nc localhost 6023, lsof -i TCP:6023, netstat -an | grep 6023

# python3 -m venv venv
# source venv/bin/activate
# pip install telnetlib3, aiofiles

from contextlib import AsyncExitStack, asynccontextmanager
from datetime import datetime
import asyncio
import sys



MIN_PYTHON = (3, 7)
if sys.version_info < MIN_PYTHON:
    sys.exit(
        f"\nThis script requires Python {MIN_PYTHON[0]}.{MIN_PYTHON[1]} or higher. "
        f"You are using Python {sys.version_info.major}.{sys.version_info.minor}.\n"
    )


try:
    import telnetlib3
    import aiofiles
except ImportError:
    print("telnetlib3/ or aiofiles is missing. Please install it in your venv.")
    sys.exit(1)


"""::1 is the IPv6 loopback address, equivalent to IPv4
              50183 is the ephemeral port used by the client
              0, 0 are the flowinfo and scopeid ipv6 specific
              """

# -------------------------
# Async logging context manager with timestamp
# aiofiles is high-level API
@asynccontextmanager
async def async_file_logger(filename):
    f = await aiofiles.open(filename, mode="a")
    try:
        yield f
    finally:
        await f.close()

# high-level API, not low-level API
async def log_message(f, level, message, addr=None):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    client_info = f" [{addr[0]}:{addr[1]}]" if addr else ""
    log_line = f"{timestamp} [{level}] {message}{client_info}"
    await f.write(log_line + "\n")
    await f.flush()
    print(log_line)  # optional: also print to console



async def shell(reader, writer, log_file):
    addr = writer.get_extra_info("peername")
    await log_message(log_file, "[INFO]", "New connection from", addr)

    writer.write('\r\nWould you like to play a game? ')
    inp = await reader.read(1)
    if inp:
        writer.echo(inp)
        writer.write('\r\nThey say the only way to win is to not play at all.\r\n')
        await log_message(log_file, "[INFO]", f"Received input from {inp}", addr)

    writer.close()
    await log_message(log_file, "[INFO", "Connection closed", addr)

# -------------------------
# Main async server
# -------------------------
async def main():
    async with AsyncExitStack() as stack:
        # Open async log file
        log_file = await stack.enter_async_context(async_file_logger("telnet_server_async.log"))

        # Start Telnet server
        server = await telnetlib3.create_server(port=6023, shell=lambda r, w: shell(r, w, log_file))
        await stack.enter_async_context(server)  # ensures proper cleanup
        await log_message(log_file, "[INFO]", "Telnet server running on port 6023...")

        # Keep server running
        await server.wait_closed()



if __name__ == "__main__":
    asyncio.run(main())
