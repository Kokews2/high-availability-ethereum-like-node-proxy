from web3 import Web3

infura_url = 'https://mainnet.infura.io/v3/<--API Token-->'

web3 = Web3(Web3.HTTPProvider(infura_url))

block_number = web3.eth.block_number

print(block_number)
