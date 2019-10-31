import sys, os, json

from Savoir import Savoir
from dotenv import load_dotenv
from pathlib import Path 

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
config = os.path.join(THIS_FOLDER, 'blockchaininfo.json')
load_dotenv()

print(os.getenv('rpcpassword'))
with open(config) as info:
    data = json.load(info)
    print(data)
    rpcuser='multichainrpc'
    rpcpassword=os.getenv('rpcpassword')
    rpchost = str(data['nodeaddress'].split('@')[1].split(':')[0])
    rpcport = str(data['port'] - 1)
    chainname = 'root'

    api = Savoir(rpcuser, rpcpassword, rpchost, rpcport, chainname)
