print("The letter")
letter = str(input())
print("The string")
userInput = str(input())
x = len(userInput)
print("")
print("the length is",len(userInput))
print(x/4)
n1 = 0
n2 = 1
n3 = 2
n4 = 3
i = 1
f = 1
while x > 0:
    while f > 0:
        cout = userInput[n1] + userInput[n2] + userInput[n3] + userInput[n4]
        writeV = letter + str(i) + " = " + str(cout)
        print(writeV)
        n1 += 4
        n2 += 4
        n3 += 4
        n4 += 4
        x -= 4
        i += 1
        f -= 1
    cout = userInput[n1] + userInput[n2]
    writeV = letter + str(i) + " = " + str(cout)
    print(writeV)
    n1 += 2
    n2 += 2
    x -= 2
    i += 1
