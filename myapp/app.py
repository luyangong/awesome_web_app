from aiohttp import web

# async def hello(request):
#     return web.Response(text="Hello, world")
#
# app = web.Application()
# app.add_routes([web.get('/', hello)])
# web.run_app(app, host='127.0.0.1')
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'www'))
from www.app import myapp
web.run_app(myapp(), host='127.0.0.1')