
import hashlib
import binascii
from typing_extensions import Self
import numpy as np
import pandas as pd
import pylab as pl
import datetime
import collections

# required by PKI
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

class Client:
    
    def __init__(self):
        
        random = Crypto.Random.new().read
        self._private_key = RSA.generate(1024, random)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)

    
    
    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')
    
class Transaction:

    def __init__(self, sender, recipient, value):

        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = datetime.datetime.now()

    def to_dict(self):
        if self.sender == "Genesis":
            identity = "Genesis"
        else:
            identity = self.sender.identity

        return collections.OrderedDict({'sender': identity,'recipient': self.recipient,'value': self.value,'time' : self.time})

    def sign_transaction(self):
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')
    
def display_transaction(transaction):
    #transaction:
    dict = transaction.to_dict()
    print ("sender: " + dict['sender'])
    print ('-----')
    print ("recipient: " + dict['recipient'])
    print ('-----')
    print ("value: " + str(dict['value']))
    print ('-----')
    print ("time: " + str(dict['time']))
    print ('-----')

class Block:
    def __init__(self):
        self.verified_transactions = []
        self.previous_block_hash = ""
        self.Nonce = ""
last_block_hash = ""

def sha256(message):
    return hashlib.sha256(message.encode('ascii')).hexdigest()

def mine(message, difficulty=1):
    assert difficulty >= 1
    prefix = '1' * difficulty
   
    for i in range(1000):
        digest = sha256(str(hash(message)) + str(i))
        if digest.startswith(prefix):
            return digest

jose = Client()
luiz = Client()
carlos = Client()
ana = Client()

transactions = []
t1 = Transaction(jose,luiz.identity,15.0)
t1.sign_transaction()
transactions.append(t1)

t2 = Transaction(jose,carlos.identity,6.0)
t2.sign_transaction()
transactions.append(t2)

t3 = Transaction(luiz,ana.identity,2.0)
t3.sign_transaction()
transactions.append(t3)

t4 = Transaction(carlos,luiz.identity,4.0)
t4.sign_transaction()
transactions.append(t4)

t5 = Transaction(ana,carlos.identity,7.0)
t5.sign_transaction()
transactions.append(t5)

t6 = Transaction(luiz,carlos.identity,3.0)
t6.sign_transaction()
transactions.append(t6)

t7 = Transaction(carlos,jose.identity,8.0)
t7.sign_transaction()
transactions.append(t7)

t8 = Transaction(carlos,luiz.identity,1.0)
t8.sign_transaction()
transactions.append(t8)

t9 = Transaction(ana,jose.identity,5.0)
t9.sign_transaction()
transactions.append(t9)

t10 = Transaction(ana,luiz.identity,3.0)
t10.sign_transaction()
transactions.append(t10)


# Miner 0
# jose = Client()
t0 = Transaction("Genesis",jose.identity,500.0)

block0 = Block()
block0.previous_block_hash = None
block0.Nonce = None

block0.verified_transactions.append(t0)
digest = hash(block0)

last_block_hash = digest

QuatiCoin = []

def dump_blockchain (self):
    
    print ("Number of blocks in the chain: " + "4")
    for x in range (len(QuatiCoin)):
        block_temp = QuatiCoin[x]
        if x == len(QuatiCoin)-1:
            print ("block # " + str(x))
    for transaction in block_temp.verified_transactions:
        display_transaction (transaction)
        print('--------------')
        print('=====================================')


QuatiCoin.append(block0)

dump_blockchain(QuatiCoin)

last_transaction_index = 0
# Miner 1
block = Block()

for i in range(3):
    temp_transaction = transactions[last_transaction_index]
    # validate transaction
    # if valid
    block.verified_transactions.append(temp_transaction)
    last_transaction_index += 1

block.previous_block_hash = last_block_hash

block.Nonce = mine(block, 2)
digest = hash(block)
QuatiCoin.append(block)
last_block_hash = digest

dump_blockchain(QuatiCoin)

# Miner 2
block = Block()

for i in range(3):
    temp_transaction = transactions[last_transaction_index]
    # validate transaction
    # if valid
    block.verified_transactions.append(temp_transaction)
    last_transaction_index += 1

block.previous_block_hash = last_block_hash

block.Nonce = mine(block, 2)
digest = hash(block)
QuatiCoin.append(block)
last_block_hash = digest

dump_blockchain(QuatiCoin)

# Miner 3
block = Block()

for i in range(3):
    temp_transaction = transactions[last_transaction_index]
    # validate transaction
    # if valid
    block.verified_transactions.append(temp_transaction)
    last_transaction_index += 1

block.previous_block_hash = last_block_hash

block.Nonce = mine(block, 2)
digest = hash(block)
QuatiCoin.append(block)
last_block_hash = digest


dump_blockchain(QuatiCoin)