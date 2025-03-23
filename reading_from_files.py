import sys


def x(thing):
    with open("database.txt", "a") as file:
        file.write(thing+"\n")


def show():
    with open("database.txt") as file:
        for line in file:
            print(line)




if __name__ == "__main__":
# sys.argv are all the arguments after your filename
    if sys.argv[1].lower() == '--list':
        show()
    else:
        x(" ".join(sys.argv[1:]))
