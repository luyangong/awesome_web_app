import orm, asyncio, sys
from models import User, Blog, Comment

async def test(loop):
	await orm.create_pool(loop, user='root', password='password', database='awesome')
	u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
	await u.save()
	await orm.close_pool()

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(test(loop))  
	loop.close()
	print('Now, loop has closed, exit this program...')
	if loop.is_closed():
		sys.exit(0)
