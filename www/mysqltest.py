import asyncio

from www import orm
from www.models import User, Blog, Comment

loop = asyncio.get_event_loop()


async def test_save(loop):
    await orm.create_pool(user='root', password='root', db='slwebapp', loop=loop)

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    await u.save()


async def test_get(loop):
    await orm.create_pool(user='root', password='root', db='slwebapp', loop=loop)

    u = await User().findAll()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = [test_save(loop), test_get(loop)]

    loop.run_until_complete(asyncio.wait(tasks))
    print('Test finished')
