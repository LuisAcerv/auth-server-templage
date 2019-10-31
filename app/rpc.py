import os

from Savoir import Savoir
from dotenv import load_dotenv
from pathlib import Path 

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

rpcuser='multichainrpc'
rpcpassword=os.getenv('rpcpassword')
rpchost = '172.17.0.2'
rpcport = '4346'
chainname = 'mainchain-dev'

api = Savoir(rpcuser, rpcpassword, rpchost, rpcport, chainname)
