#!/bin/python


import logging


logging.basicConfig(level=logging.INFO)



logging.debug("""backend developers usually do not use constant prompting
              django api or flask usually doesn't ask users for input with input()
              they use http requests, databases, message queues or files
              typing in a loop until expected input/output is not common
              - usually send the error http response for the request 400 bad request""")

def get_target():
    while True:
        target = input("Enter a target: ")
        if not target:
            print("Error")
            continue
        else:
            break


def get_name():
    while name:
        name = input("Enter a name: ")
        if not name:
            print("Error")
            continue
        else:
            break



def get_last_name():
    while True:
        last_name = input("Enter a last name. all uppercase: ").strip()

        logging.debug("the last_name variable must be uppercase")
        if not last_name.isupper():
            print("Error")
            continue
        else:
            break


def get_age():
    while True:
        
        logging.debug("instead of using int wrapper using the string isalnum")
        age = input("Enter an age: ").strip()
        if not age.isalnum():
            print("error")
            continue
        else:
            break



logging.debug("combining exception handling and custom validation.")
def get_above_18():
    while True:
        try:
            age = int(input("enter an age: "))
        except ValueError:
            print("expecting an integer. try again...")
            continue
        if age < 0:
            print("enter a number above zero")
            continue
        else:
            break
    if age >= 18:
        print("expression is true")
    else:
        print("Expression is not true")

logging.debug("""encapsulating exception handling
              custom validation""")
def encapsulation(parameter):
    while True:
        try:
            any_value = int(input(parameter))
        except ValueError:
            print("you've entered a non numeric value. try again...")
            continue
        if any_value < 0:
            print("enter a non negative integer...")
            continue
        else:
            break
    return any_value
logging.debug("call it in the dunder main")
#number = encapsulation("enter a number: ")

logging.debug("keep prompting.")
def get_n():
    while True:
        p_n = input("Enter a value: ")
        if p_n:
            break
        print("Enter something...")

logging.debug("missing the constant prompting until user enters input")
def raise_error():
    target = input("Enter a target for destruction: ").strip()
    if not target:
        raise ValueError("Error. Enter a target. try again...")
        



if __name__ == "__main__":
    #number = encapsulation("enter a number: ")
    raise_error()