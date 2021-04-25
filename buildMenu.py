##
# Record <SURNAME,AGE,PROFESSION> of some employees in a file
# Get the data entered by the user and return the other two
# If there is a match on several lines, the others must also be returned
#
# surname   age     profession
# xxx       yy      zzz
# xxx       yy      zzz

import os


def message():
    os.system('cls')
    riga = '*'
    linea = '*'
    print(riga * 21)
    print(linea, "  Staff archive  ", linea)
    print(riga * 21)


def menu():
    print("%s" % " New              [1]")
    print("%s" % " Search           [2]")
    print("%s" % " View             [3]")
    print("%s" % " Quit             [0]\n")


answer = ""
rec = 0
nfile = "filenames.txt"
message()
menu()

while answer != '0':
    answer = input("%3s" % "> ")
    # QUIT
    if answer == '0':
        print("\nQuit!")
    # NEW DATA
    elif answer == '1':
        datafile = open(nfile, "a")
        name = input("Enter Name > ")
        age = input("Age > ")
        profession = input("Profession > ")
        datafile.write("%-13s%-5s%-10s\n" % (name.lower(), age, profession))
        datafile.close()
        message()
        menu()
    # SEARCH DATA
    elif answer == '2':
        ricerca = input("\nEnter NAME , AGE o PROFESSION > ")
        # I look for little words only
        ricerca = ricerca.lower()
        datafile = open(nfile, "r")
        for line in datafile:
            rec = rec + 1
            line = line.rstrip()
            wordlist = line.split()
            # the search in the list gave a positive result?
            if ricerca in wordlist:
                n = wordlist.index(ricerca)
                print(f'\n\'{ricerca.upper()}\' present in the record n. {rec}')
                if n == 0:
                    print("Age = ", wordlist[1], "\nProfession = ", wordlist[2], "\n")
                if n == 1:
                    print("Surname =", wordlist[0], "\nProfession = ", wordlist[2], "\n")
                if n == 2:
                    print("Surname =", wordlist[0], "\nAge = ", wordlist[1], "\n")
        datafile.close()
        rec = 0
        pausa = input("Press a key....")
        message()
        menu()
    # VIEW DATA
    elif answer == '3':
        os.system('cls')
        print("**************************")
        print("*       View data        *")
        print("**************************\n")
        datafile = open(nfile, "r")
        print("%-13s%-5s%-10s" % ("Name", "Age", "Prof"))
        print('-' * 26)
        for line in datafile:
            print(line.rstrip())
        datafile.close()
        pausa = input("\nPress a key....")
        message()
        menu()
    else:
        message()
        menu()
