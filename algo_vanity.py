#!/usr/bin/env python3

from algosdk import account, mnemonic
import time

# Desired prefix for address.
PREFIX = "" # CHANGE TO WHAT PREFIX IS NEEDED // BETTER RESULTS WHEN CHAR IS < 5

# Variables containing Private Key and Address
PRIVATE_KEY = ""
ADDRESS = ""

# Keep looping until desired address is found.
while (not ADDRESS.startswith(PREFIX)):
    PRIVATE_KEY, ADDRESS = account.generate_account()
    

print(ADDRESS)
print(PRIVATE_KEY)
print(mnemonic.from_private_key(PRIVATE_KEY))
