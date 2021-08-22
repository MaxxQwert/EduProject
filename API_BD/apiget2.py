import asyncio
from platform import system
from dataclasses import dataclass
from time import sleep
from timeit import default_timer

import asyncpg
from aiohttp import ClientSession
from loguru import logger
from functools import wraps

from tortoise import Tortoise, run_async, fields
from tortoise.models import Model
from tortoise_model import User

from asyncio.proactor_events import _ProactorBasePipeTransport





def silence_event_loop_closed(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except RuntimeError as e:
            if str(e) != 'Event loop is closed':
                raise

    return wrapper


if system() == 'Windows':
    _ProactorBasePipeTransport.__del__ = silence_event_loop_closed(_ProactorBasePipeTransport.__del__)


def timing_dec(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = default_timer()
        func_result = await func(*args, **kwargs)
        end_time = default_timer()
        logger.info('Function execution time with args {}  is {:.4f}', args, end_time - start_time)
        return func_result

    return wrapper


@dataclass
class Service:
    name: str
    url: str
    ip_field: str


@timing_dec
async def fetch_user(url: str):
    async with ClientSession() as session:
        a = await session.get(url)
        b = await a.json()

    return await a.json(), 'user'


@timing_dec
async def fetch_todos(url: str):
    async with ClientSession() as session:
        a = await session.get(url)
        b = await a.json()

    return await a.json(), 'todos'

@timing_dec
async def fetch_photos(url: str):
    async with ClientSession() as session:
        a = await session.get(url)
        return await a.json(), 'photos'


@timing_dec
async def fetch_albums(url: str):
    async with ClientSession() as session:
        a = await session.get(url)
        return await a.json(), 'albums'


@timing_dec
async def fetch_comments(url: str):
    async with ClientSession() as session:
        a = await session.get(url)
        return await a.json(), 'comments'


@timing_dec
async def fetch_posts(url: str):
    async with ClientSession() as session:
        a = await session.get(url)
        return await a.json(), 'posts'


if __name__ == '__main__':
    coros = [fetch_user('https://jsonplaceholder.typicode.com/users'),
             fetch_todos('https://jsonplaceholder.typicode.com/todos'),
             fetch_photos('https://jsonplaceholder.typicode.com/photos'),
             fetch_albums('https://jsonplaceholder.typicode.com/albums'),
             fetch_comments('https://jsonplaceholder.typicode.com/comments'),
             fetch_photos('https://jsonplaceholder.typicode.com/posts')]
    coro = asyncio.wait(coros,
                        timeout=50,
                        return_when=asyncio.ALL_COMPLETED,
                        # return_when=asyncio.FIRST_COMPLETED,
                        )
    done, pending = asyncio.run(coro)
    res = []
    for t in done:
        res.append(t.result())
    else:
        logger.warning("No results!")

    # sleep(1)
    print(res)
