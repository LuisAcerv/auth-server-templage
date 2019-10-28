import logging
import json
from app.tcp import api

logging.basicConfig(level=logging.INFO)


def info():
    info = api.getinfo()
    logging.info(info)

    return json.dumps(info)