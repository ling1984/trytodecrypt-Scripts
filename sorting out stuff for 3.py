def lower():
    print("Input your lowercase string file name")
    fileName = str(input())
    fileName = fileName + ".txt"
    f = open(fileName,"r")
    userInput = f.read()
    print("The length is",len(userInput))
    x = len(userInput)
    letter = "a"
    n1 = 0
    n2 = 1
    n3 = 2
    printer(userInput,letter,n1,n2,n3,x)
    print("")
    menu()

def upper():
    print("Input your uppercase string file name")
    fileName = str(input())
    fileName = fileName + ".txt"
    f = open(fileName,"r")
    userInput = f.read()
    print("The length is",len(userInput))
    x = len(userInput)
    letter = "A"
    n1 = 0
    n2 = 1
    n3 = 2
    printer(userInput,letter,n1,n2,n3,x)
    print("")
    menu()

def number():
    print("Input your number string (starting at zero) file name")
    fileName = str(input())
    fileName = fileName + ".txt"
    f = open(fileName,"r")
    userInput = f.read()
    print("The length is",len(userInput))
    x = len(userInput)
    letter = "0"
    n1 = 0
    n2 = 1
    n3 = 2
    printer(userInput,letter,n1,n2,n3,x)
    print("")
    menu()

def printer(userInput,letter,n1,n2,n3,x):
    while x != 0:
        theActualOutput = userInput[n1] + userInput[n2] + userInput[n3]
        print(letter,"=",theActualOutput)
        letter = chr(ord(letter)+1)
        n1 = n1 + 3
        n2 = n2 + 3
        n3 = n3 + 3
        x = x - 3

def menu():
    print("OPTIONS")
    print("1. Lowercase")
    print("2. Uppercase")
    print("3. Number")
    print("4. Quit")
    choice = int(input())
    if choice == 1:
        lower()
    elif choice == 2:
        upper()
    elif choice == 3:
        number()
    elif choice == 4:
        quit()
    else:
        print("Wanna try me on error handling?")
        print("")
        menu()

menu()

