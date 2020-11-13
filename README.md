# Blockchain-voting

1. Ensure to install all requirements
   pip3 install -r requirements.txt
2. To run the first instance of the node execute 
   python3 -m backend.app
3. To run other instances of the node execute
   export PEER=True && python3 -m backend.app
4. Routes available
    domain
    domain/blockchain
    domain/blockchain/mine
    domain/wallet/transact