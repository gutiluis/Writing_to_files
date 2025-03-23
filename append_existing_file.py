def x(thing):
    file = open("database.txt", "a"):
    file.write(thing+"\n")
    file.close()


if __name__ == "__main__":
    x(input("enter and append to the end of the file a new line")
