userIn = None

charList = []
classList = []
raceList = []

while userIn != "4":
    print("1 - Display Characters")
    print("2 - Add Character")
    print("3 - Delete Character")
    print("4 - Quit")
    userIn = input("> ")
    print()
    if userIn == "1":
        print("  {:<15} {:<15} {:<10}".format("Character", "Class", "Race"))
        for x in range(len(charList)):
            print(x+1, "{:<15} {:<15} {:<10}".format(charList[x], classList[x], raceList[x]))
        print()
    elif userIn == "2":
        charList.append(input("Name: "))
        classList.append(input("Class: "))
        raceList.append(input("Race: "))
        print()
    elif userIn == "3":
        x = int(input("List Number: ")) - 1
        del charList[x]
        del classList[x]
        del raceList[x]
        print()

