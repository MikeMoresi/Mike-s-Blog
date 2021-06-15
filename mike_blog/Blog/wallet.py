import web3
from web3 import Web3

w3 = Web3(web3.HTTPProvider('https://ropsten.infura.io/v3/0f7fe951049e4450bcc4b62158e92e7c'))
account = w3.eth.account.create()
privateKey = account.privateKey.hex()
address = account.address

print(f"your address: {address} \nYour Key: {privateKey}")