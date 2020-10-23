import json
from hashlib import sha256
def sha256Hash(*args):
    """
    return sha256 of the given data.
    """
    jsonList = map(lambda x: json.dumps(x), args)
    jsonString = ''.join(sorted(jsonList))
    return sha256(jsonString.encode('utf-8')).hexdigest()

if __name__ == '__main__':

    print(hash(1,'2',[3]))
    print(hash([3],1,'2'))