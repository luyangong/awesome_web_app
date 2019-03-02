from aiohttp import web
import aiohttp

# async def hello(request):
#     return web.Response(text="Hello, world")
#
app = web.Application()
# app.add_routes([web.get('/', hello)])
# web.run_app(app, host='127.0.0.1')
import sys
import os
async def websocket_handler(request):

    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                print('gooooooooooooooooooooooooooooooood!')
                await ws.send_str(msg.data + '/answer')
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())

    print('websocket connection closed')

    return ws
app.add_routes([web.get('/ws', websocket_handler)])
web.run_app(app, host='127.0.0.1')