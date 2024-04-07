import uuid
import time
import json
import datetime as dt
from pprint import pprint

import websocket


def on_open(*args):
    global t_1
    t_2 = time.time()
    print('OPEN:', t_2 - t_1)


def on_message(ws, message):
    msg = json.loads(message)
    pprint(msg)


def on_error(ws, error):
    print('on_error:', error)
    ws.close()


def on_close(ws, close_status_code, close_msg):
    print('*** closed ***', close_status_code, close_msg)
    ws.close()


t_1 = 0


def main():
    global t_1
    t_1 = time.time()

    url = 'ws://127.0.0.1:8000/ws2/'
    ws = websocket.WebSocketApp(url,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever(ping_timeout=60)


if __name__ == '__main__':
    main()
