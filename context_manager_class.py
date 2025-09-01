#!/bin/python

import logging

logging.basicConfig(level=logging.INFO)

class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        self.file_obj.close()


logging.debug("overwrite file")
#with File("script.txt", "w") as opened_file:
 #   opened_file.write("hello")

logging.info("append file flag")
with File("script.txt", "a") as file:
    file.write("\nappend this")
