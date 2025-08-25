# a context manager is an object that defines the runtime context to be established when executing a with statement
# the context manager handles the entry into, and the exit from, the desired runtime context for the execution of the block of code

# object.__enter__(self)
# object.__exit__(self, exc_type, exc_value, traceback)

# context manager types

# the with statement is used to wrap the execution of a block with methods defined by a context manager
# with allows encapsulation of try, except, finally
import logging # what is pytest?
import os
import sys

logging.basicConfig(level=logging.INFO) # otherwise it will not print. level of severity not enough


def update_inventory(product):
    if not os.path.exists("database.txt"):
        with open("database.txt", "w") as file: # column headers can be ignored later
            file.write(product+"\n")
        logging.debug("Database initialized.")
    else:
        with open("database.txt", "a") as file:
            file.write(product+"\n")
        logging.info("Product added")

# call the iterator with the python3 filename --list
def space_the_list():
    with open("database.txt") as file:
        for line in file:
            print(line)

if __name__ == "__main__":
    if sys.argv[1].lower() == "--list": # sys.argv is all the arguments after the filename
        space_the_list()
    else:
        update_inventory(" ".join(sys.argv[1:]))
    
    
"""

def update_inventory(product, brand, quantity):
    with open("database.txt", "a") as file:
        file.write(f"{product},{brand},{quantity}\n")
    print(f"{product},{brand},{quantity} added successfully")


if __name__ == "__main__":
    make_inventory()
    product = input("Enter a product: ")
    brand = input("Enter brand: ")
    quantity = input("Enter quantity: ")
    update_inventory(product, brand, quantity)

"""