from utils.crypto import sha256Hash

def test_crypto():
    assert sha256Hash(1,[2],'three') == sha256Hash([2],1,'three')
    assert sha256Hash('cryptocurrency')=='5642e09b7351ef446cab12aa80bd735ede4b6ef946794c30a53de7282bb59e53'