"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

An asyncio Example: Probing Domains
"""
import asyncio
import socket
import keyword

MAX_KEYWORD_LEN = 4  # we want a short domain name


async def probe(domain: str) -> tuple[str, bool]:
    """
    Check if the passed domain is active

    Return the domain name (keep the code simple) and a boolean for its resolution
    """
    loop = asyncio.get_running_loop()  # a reference to the actual event loop
    try:
        # if the DNS does not resolve the domain, it raises an exception
        await loop.getaddrinfo(domain, None)
    except socket.gaierror:
        # this means, we could not access the domain, maybe it is not registered!
        return domain, False

    # we got the address info, the domain is known to the DNS
    return domain, True


async def main() -> None:
    """Being a coroutine, we can await in it"""

    # a generator yielding ".dev" domains based on short Python keywords
    domains = (f'{name}.dev'.lower() for name in keyword.kwlist if len(name) <= MAX_KEYWORD_LEN)

    # list of coroutines probing the domains
    probes = [probe(domain) for domain in domains]
    # the probes are run concurrently and returned as completed
    for coro in asyncio.as_completed(probes):
        # we know that the coroutine is already completed, so await here is non-blocking
        domain, found = await coro
        print(f'{'+' if found else ' '} {domain}')


if __name__ == '__main__':
    # start the event loop, pend until it exits
    asyncio.run(main())
