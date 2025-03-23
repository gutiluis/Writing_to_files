def x(thing):
    file = open("database.txt", "w") # overwrite. truncate
    file.write(thing+"\n")
    file.close()



if __name__ == "__main__":
    x(input("enter and register"))
