#!/usr/local/bin/python2
# Author: Rami

import Crypto
from Crypto.PublicKey import RSA
from base64 import b64decode
import ast
import sys

args = sys.argv[1].split("~")

pubkey_obj = RSA.importKey(b64decode(args[0]))

encrypted = pubkey_obj.encrypt(args[1], 32)
print encrypted[0]
