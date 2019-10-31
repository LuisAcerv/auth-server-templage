# Create network
`sh zuppvm/init.sh`

# Run server
`sh run-server.sh`

# Issue from
`issuefrom ORIGINAL_ADDRESS ORIGINAL_ADDRESS '{"name":"ASSET_NAME","open":true}' 50000 0.01 0 '{"origin":"ORIGN", "stage":"01", "purpose":"network payments"}'`

# Issue more from
`issuemorefrom FROM_ADDRESS TO_ADDRESS GBP 25000 0 '{"origin":"ORIGIN", "stage":"02", "approval":"department"}'`