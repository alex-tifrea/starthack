import Crypto
from Crypto.PublicKey import RSA
from base64 import b64decode
import ast
import sys

bin_key = sys.argv[1]
print bin_key
pubkey_obj = RSA.importKey(bin_key)

encrypted = publickey.encrypt(sys.argv[2], 32)
