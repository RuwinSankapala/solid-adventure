from time import sleep
from requests import get as requestget
from os import environ
from logging import error as loggingerror

BASE_URL = environ.get('BASE_URL_OF_BOT', None)
try:
    if len(BASE_URL) == 0:
        raise TypeError
    BASE_URL = BASE_URL.rstrip("/")
except TypeError:
    BASE_URL = None
PORT = environ.get('PORT', None)
if PORT is not None and BASE_URL is not None:
    while True:
        try:
            requestget(BASE_URL).status_code
            sleep(600)
        except Exception as e:
            loggingerror(f"alive.py: {e}")
            sleep(2)
            continue
