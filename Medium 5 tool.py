overall = 0

def main(overall):
    while overall <= 4:
        print("What letter?")
        letter = str(input())
        print("The string")
        userInput = str(input())
        x = len(userInput)
        print("")
        print("the length is",len(userInput))
        print(x / 18)
        n1 = 0
        n2 = 1
        n3 = 2
        i = 1
        file = open("Saved.txt","a+")
        #pattern of 6 and 3 in each letter
        while x > 0:
            cout = userInput[n1] + userInput[n2] + userInput[n3]
            writeV = letter + str(i) + " = " + str(cout) + "\n"
            print(writeV)
            file.write(writeV)
            n1 += 3
            n2 += 3
            n3 += 3
            x -= 3
            i +=1
        print("")
        overall = overall + 1
        main(overall)
main(overall)
