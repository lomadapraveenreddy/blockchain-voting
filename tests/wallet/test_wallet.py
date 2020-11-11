from wallet.wallet import Wallet

def test_verifyValidSignature():
    data = {'foo': 'test data'}
    wallet = Wallet()
    signature = wallet.sign(data)

    assert Wallet.verify(wallet.public_key, data, signature)

def test_verifyInvalidSignature():
    data = {'foo': 'test data'}
    wallet = Wallet()
    signature = wallet.sign(data)

    assert not Wallet.verify(Wallet().public_key, data, signature) 