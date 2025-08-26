#!/bin/python

# script to open a csv file withou a context manager for now.
# to do. add the context manager.


# import csv
import logging



logging.basicConfig(level=logging.INFO)


def get_file():
    logging.info("create reader object with input function")
    while True:
        try:
            logging.debug("Open returns a file object. Not a string.")
            get_string = input("Enter the name of the CSV file: ").strip()
            if get_string.lower() == "exit":
                break
            if not get_string:
                raise ValueError("Input(). ~ Empty string error.")
            
            reader_object = open(get_string)
            return reader_object

            
        except FileNotFoundError:
            logging.error("raised when open() is called on a filename that does not exist.")
            print("Try again. Missing file name.")
        except ValueError as err:
            logging.error("Empty string input error. ")
            print(err)


if __name__ == "__main__":
    get_file()