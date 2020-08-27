from time import time
import hashlib
import json
print("This bus travels on a route of 4 stations: Station A, Station B, Station C and Station D")
print("Have a safe journey")
input(Bus Number", BusNo")
input("Boarding from:", Board)
input("Boarding to:", Depart)
ppkm = 2.5


if(board == "Station A" and depart == "station B"):
    distance = 40
    amount = distance*ppkm
    print("amount is :", amount)
elif(board == "Station B" and depart == "station C"):
    distance = 30
    amount = distance*ppkm
    print("amount is:",amount)
elif(board == "Station C" and depart == "Station D"):
    distance =45
    amount = distance*ppkm
    print("amount is:",amount)
elif(board == "station A" and depart == "Station C"):
    distance = 70
    amount = distance*ppkm
    print("amount is:",amount)
elif(board == "Station A" and depart == "Station D"):
    distance = 115
    amount = distance*ppkm
    print("amount is:",amount)
else:
    print("Invalid Input")
if (board =="station A" or board == "Station B" or Board == "Station C" or Board =="Station D"):
    class Blockchain(object):
    '''
    A Blockchain Class
    '''
        def __init__(self):
        '''
            Initiates a new blockchain
        '''
            self.chain = []
            self.current_transactions = []

            self.new_block(proof=100, previous_hash=None)

        def new_block(self, proof:int, previous_hash:str) -> dict:
        '''
        Creates a new block and add it to the chain

        :param proof: proof of work 
        :param previous_hash: the hash of the previous block
        :return: New block thats created
        '''
            block = {
                'index' : len[self.chain] + 1,
                'timestamp' : time(),
                'transactions' : self.current_transactions
                'proof' : proof, 
                'previous_hash' = previous_hash
            }

            self.current_transactions = []
            self.chain.append(block)
            return block

        def new_transaction(self, sender:str, recipient:str, amount:int) -> int:
        '''
        Creates a new transaction to go into the next mined block

        :param sender: Address of sender
        :param recipient: Address of recipient
        :param amount: Amount
        :return: index of the block that will hold this transaction
        '''
            self.current_transactions.append/
            ({'Place of boarding': sender, 
        'Place tillboarding': recipient,
          'amount':amount})

            return self.last_block['index'] + 1
    
        @staticmethod
        def hash(block:dict) -> str:
        '''
        Hashes a the given block with sha256
        '''
            block_string = json.dumps(block, sort_keys=True).encode()
            return hashlib.sha256(block_string).hexdigest()

        @property
        def last_block(self):
        '''
        Returns the last block in the chain
        '''
        return self.chain[-1]
    else:
        print("invalid option")