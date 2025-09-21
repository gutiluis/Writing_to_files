#!/bin/env python


import hashlib
import logging


logging.basicConfig(level=logging.INFO)



logging.debug("function to cryptographic hash user_names")
logging.debug("integrity - verification, authentication, and digital security")
logging.info("Do not hash a passwords with SHA-256...")
#TODO: make a context manager to write the output in a separate file...")
def get_user_name_hash():
    user_name = input("Enter a user_name: ")    
    hash_name = hashlib.sha256(user_name.encode()).hexdigest()
    #print(id(hash_name))
    #print(hash_name.__hash__())
    return hash_name



print(get_user_name_hash())


