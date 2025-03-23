# with statement exempts you from closing the file and opening it
def x(thing):
# a to append. w to overwrite
    with open("database.txt", "a") as file:

        file.write(thing+"\n")




if __name__ == "__main__":
    x(input("enter something: "))
