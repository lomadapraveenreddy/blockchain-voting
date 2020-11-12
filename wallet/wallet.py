import json
import uuid
from config import STARTING_BALANCE

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import (
    encode_dss_signature,
    decode_dss_signature
) 
from cryptography.hazmat.primitives import hashes,serialization
from cryptography.exceptions import InvalidSignature


class Wallet:

    def __init__(self):
        self.address = str(uuid.uuid4())[0:8]
        self.balance = STARTING_BALANCE
        self.private_key = ec.generate_private_key(ec.SECP256K1(), default_backend())
        self.public_key = self.private_key.public_key()
        self.serializePublicKey()
    
    def sign(self,data):
        '''
        generate a signature
        '''
        return decode_dss_signature(self.private_key.sign(json.dumps(data).encode('utf-8'), ec.ECDSA(hashes.SHA256())))

    def serializePublicKey(self):
        self.public_key_bytes=self.public_key.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo)
        self.decodedPublicKey=self.public_key_bytes.decode('utf-8')
        self.public_key=self.decodedPublicKey

    @staticmethod
    def verify(public_key, data, signature):
        '''
        verifies a signature based on original public key and data
        '''
        public_key=serialization.load_pem_public_key(
            public_key.encode('utf-8'),
            default_backend()
        )
        (r,s)=signature
        try:
            public_key.verify(encode_dss_signature(r,s), json.dumps(data).encode('utf-8'),ec.ECDSA(hashes.SHA256()))
            return True
        except InvalidSignature:
            return False


def main():
    wallet = Wallet()
    print(f'wallet.__dict__: {wallet.__dict__}')

    data = {'foo': 'bar'}
    signature = wallet.sign(data)
    print(f'signature: {signature}')

    shouldBeValid = Wallet.verify(wallet.public_key, data, signature)
    print(f'should be valid: {shouldBeValid}')

    shouldBeInvalid = Wallet.verify(Wallet().public_key, data, signature)
    print(f'should be invalid: {shouldBeInvalid}')

if __name__ == "__main__":
    main()



 