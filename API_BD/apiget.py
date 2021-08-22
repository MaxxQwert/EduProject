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


async def tabinit():
    # await Tortoise.init(
    #     db_url="postgres://postgres:0000@localhost/Placeholder",
    #     modules={'models': ['__main__']}
    # )
    # # Generate the schema
    # await Tortoise.generate_schemas()
    conn = await asyncpg.connect(
        "postgresql://postgres:0000@localhost/Placeholder"
        # user='user',
        # password='password',
        # database='database',
        # host='127.0.0.1'
    )


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

    conn = await asyncpg.connect(
        "postgresql://postgres:0000@localhost/Placeholder"
    )
    for p in b:
        print('user')
        await conn.execute(
            "INSERT INTO users(name, username, email, address, phone, website, company) VALUES($1, $2, $3, $4, $5, "
            "$6, $7)",
            p['name'],
            p['username'],
            p['email'],
            '; '.join([f'{key}: {value}' for key, value in p['address'].items()]),
            p['phone'],
            p['website'],
            '; '.join([f'{key}: {value}' for key, value in p['company'].items()])
        )
    await conn.close()
    return await a.json()


@timing_dec
async def fetch_todos(url: str):
    async with ClientSession() as session:
        print('1')
        a = await session.get(url)
        b = await a.json()
    # print(s)
    print('2', a)
    conn = await asyncpg.connect(
        "postgresql://postgres:0000@localhost/Placeholder"
    )
    print('3', b)
    for p in b:
        # print('4')
        await conn.execute(
            "INSERT INTO todos(useridrr, title, completed) VALUES($1, $2, $3)",
            p['userId'],
            p['title'],
            p['completed']
        )
        # print('5')
    # await todos_bd(b, conn)

    await conn.close()
    print('5')
    return await a.json()


async def todos_bd(b, conn):
    for p in b:
        await conn.execute(
            "INSERT INTO todos(userid, title, completed) VALUES($1, $2, $3)",
            p['userId'],
            p['title'],
            p['completed']
        )
    print(s)
    return 5

@timing_dec
async def fetch_photos(url: str):
    async with ClientSession() as session:
        a = await session.get(url)
        return await a.json()


@timing_dec
async def fetch_albums(url: str):
    async with ClientSession() as session:
        a = await session.get(url)
        return await a.json()


@timing_dec
async def fetch_comments(url: str):
    async with ClientSession() as session:
        a = await session.get(url)
        return await a.json()


@timing_dec
async def fetch_posts(url: str):
    async with ClientSession() as session:
        a = await session.get(url)
        return await a.json()


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
    # res = []
    # for t in done:
    #     res.append(t.result())
    # else:
    #     logger.warning("No results!")

    # sleep(1)
    print('stop')
