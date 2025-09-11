#!/bin/python

import asyncio
import logging
import sys


logging.basicConfig(level=logging.INFO)


try:
    import aiofiles
except ImportError:
    print("pip install aiofiles")
    sys.exit(1)



#----------
# high-level API
#------------
logging.debug("""simpler, higher-abstraction operations like launching tasks, managing streams,
              using synchronization primitives, and interacting with suprocesses...
              -> abstracting run_in_executor()""")
async def high_level_API():
    async with aiofiles.open("log.txt", "a") as file_abstraction:
        await file_abstraction.write("hello\n")




logging.debug("""raw event-loop management, futures, transports and protocols,
              loop policies, and direct control""")
#---------------
# low level async
#---------------
def write_file(file, txt):
    with open(file, "a") as f:
        f.write(txt)

async def low_level_API():
    object = asyncio.get_running_loop()
    await object.run_in_executor(None, write_file, "log.txt", "hello\n")





def menu():
    while True:
        print("""
              \nSelect an example from the following options: 
              \rl) low level asyncio API
              \rh) high level abstraction API
              \re) Exit""")
        choice = input("Choose an example: ")
        if choice in ["l", "h", "e"]:
            return choice
        else:
            input("""
                  \nThe intstructions were given...
                  \rPress Enter to try main menu()""")

logging.debug("when calling from synchronous code. consider async and that have to await or wrap in asyncio.run()")
def entrance():
    run_program = True
    while run_program:
        choice = menu()
        
        if choice == "l":
            asyncio.run(low_level_API())
        elif choice == "h":
            asyncio.run(high_level_API())
        else:
            print("ending program...")
            run_program = False
        

if __name__ == "__main__":
    entrance()