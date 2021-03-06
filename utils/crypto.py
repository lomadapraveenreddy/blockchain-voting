import json
from hashlib import sha256
from blockchain.vote import Vote
from utils.hex_to_bin import hexToBinary
def sha256Hash(*args):
    """
    return sha256 of the given data.
    """
    jsonList = map(lambda x: json.dumps(x), args)
    jsonString = ''.join(sorted(jsonList))
    return hexToBinary(sha256(jsonString.encode('utf-8')).hexdigest())

if __name__ == '__main__':
    print(sha256Hash('foo'))
    print(sha256Hash(1,[2],'three'))
    print(sha256Hash(Vote('1','3').__dict__,Vote('1','2').__dict__))