1. Connecting to a blockchain
Now we’ll connect to this blockchain from elsewhere. On the second server, run the following:

`multichaind chain1@[ip-address]:[port]`

Other nodes can connect to this node using:
multichaind mainchain-dev@172.17.0.2:6839

Listening for API requests on port 6838 (local only - see rpcallowip setting)

Node ready.

# Accept rpc connections
- Modify multichain.conf and add the line `rpcallowip=0.0.0.0/0`

# TODO:
- [ ] Setup blockchain configuration / permissions
- [ ] Issue main token