import asyncio
import logging
from datetime import datetime
import json
from aiowebsocket.converses import AioWebSocket
async def startup(uri):
    async with AioWebSocket(uri) as aws:
        converse = aws.manipulator
        # 客户端给服务端发送消息
        # await converse.send('{"action":"subscribe","args":["QuoteBin5m:14"]}')
        await converse.send('{"access_token":"3dd0612c-c662-4990-b125-f09df2914423"}')
        while True:
            mes = await converse.receive()
            print('{time}-Client receive: {rec}'
                  .format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), rec=mes))
if __name__ == '__main__':
    # remote = 'wss://api.bbxapp.vip/v1/ifcontract/realTime'
    remote = 'ws://192.168.33.235:7001/websocketServer/allStationAlarm'
    try:
        asyncio.get_event_loop().run_until_complete(startup(remote))
    except KeyboardInterrupt as exc:
        logging.info('Quit.')
        # 'ws://192.168.33.235:7001/websocketServer/allStationAlarm?access_token=3dd0612c-c662-4990-b125-f09df2914423'

# import websocket
# import abnf
# import json
# import _thread
# import time
#
# url = "ws://192.168.33.235:7001/websocketServer/allStationAlarm"   # 接口地址
#
# def on_message(ws, message):
#    print(message)
#
# def on_error(ws, error):
#     print(error)
#
# def on_close(ws):
#     print("close connection")
#
# def on_open(ws):
#     def run(*args):
#         content = {
#             'access_token':'3dd0612c-c662-4990-b125-f09df2914423'
#         }
#         ws.send(json.dumps(content))
#         ws.send('', abnf.OPCODE_BINARY)
#         time.sleep(1.5)
#         ws.close()
#     _thread.start_new_thread(run, ())
#
# if __name__ == "__main__":
#     websocket.enableTrace(True)
#     ws = websocket.WebSocketApp(url,
#                               on_message = on_message,
#                               on_error = on_error,
#                               on_close = on_close)
#     ws.on_open = on_open
#     ws.run_forever()

