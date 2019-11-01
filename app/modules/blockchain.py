import logging
import json
from app.rpc import api

logging.basicConfig(level=logging.INFO)


def info():
    info = api.getinfo()
    logging.info(info)

    return json.dumps(info)

def zpp_info():
    asset_info = api.listassets('ZPP')

    logging.info(asset_info)

    return json.dumps(asset_info)


def get_address_balance(data):
    _data = json.load(data)
    balance = api.getaddressbalances(_data['address'])

    logging.info(balance)

    return json.dumps(balance)

def issue_from_original_address(data):
    _data = json.load(data)
    address = _data['address']

    return json.dumps({'hello':'world'})

def create_key_pairs():
    keypairs = api.createkeypairs()
    logging.info(keypairs)
    return json.dumps(keypairs)

def create_stream_from(data):
    _data = json.load(data)
    address = _data['address']
    name = _data['name']
    result = api.createfrom(address, 'stream', name)

def create_stream(data):
    pass

def get_new_address(data):
    pass

def get_stream(data):
    pass

def get_address_streams(data):
    pass

def publishfrom(data):
    _data = json.load(data)
    from_address = _data['address']
    stream = _data['stream']
    keys = _data['keys']
    d = _data['data']
    
    tx_hash = api.publishfrom(from_address, stream, keys, d)
    
    logging.info(tx_hash)
    return json.dumps(tx_hash)
    