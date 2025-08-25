import logging 
import os
import sys

logging.basicConfig(level=logging.INFO) 


def update_inventory(product):
    if not os.path.exists("database.txt"):
        with open("database.txt", "w") as file: # column headers can be ignored later
            file.write(product+"\n")
        logging.info("Database initialized.")
    else:
        with open("database.txt", "a") as file:
            file.write(product+"\n")
        logging.info("Product added")


def space_the_list():
    with open("database.txt") as file:
        for line in file:
            print(line)

if __name__ == "__main__":
    if sys.argv[1].lower() == "--list": # sys.argv is all the arguments after the filename
        space_the_list()
    else:
        update_inventory(" ".join(sys.argv[1:]))
