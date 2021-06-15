from web3 import Web3

def sendTransaction(message):
    w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/0f7fe951049e4450bcc4b62158e92e7c'))
    address = '0x25237b847B01778cD4116F5e67eBBE8358862F51'
    privateKey = '0x747916d8cb9e493e816e5c91f7f2d7c49c4cf81c53dc4dc157c50c019e8ed34f'
    nonce = w3.eth.getTransactionCount(address)
    gasPrice = w3.eth.gasPrice
    value = w3.toWei(0,'ether')
    signedTx = w3.eth.account.signTransaction(dict(
        nonce=nonce,
        gasPrice=gasPrice,
        gas=100000,
        to='0x0000000000000000000000000000000000000000',
        value=value,
        data=message.encode('utf-8')
    ),privateKey)

    tx= w3.eth.sendRawTransaction(signedTx.rawTransaction)
    txId = w3.toHex(tx)
    return txId