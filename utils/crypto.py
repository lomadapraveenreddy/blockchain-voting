import json
from hashlib import sha256
from blockchain.vote import Vote
def sha256Hash(*args):
    """
    return sha256 of the given data.
    """
    jsonList = map(lambda x: json.dumps(x), args)
    jsonString = ''.join(sorted(jsonList))
    return sha256(jsonString.encode('utf-8')).hexdigest()

if __name__ == '__main__':

    print(sha256Hash(Vote('1','2').__dict__,Vote('1','3').__dict__))
    print(sha256Hash(Vote('1','3').__dict__,Vote('1','2').__dict__))