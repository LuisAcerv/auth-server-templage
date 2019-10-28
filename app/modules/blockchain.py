import logging
import json
from app.rpc import api

logging.basicConfig(level=logging.INFO)


def info():
    info = api.getinfo()
    logging.info(info)

    return json.dumps(info)

def asset_info():
    asset_info = api.listassets('GBP')

    logging.info(asset_info)

    return json.dumps(asset_info)