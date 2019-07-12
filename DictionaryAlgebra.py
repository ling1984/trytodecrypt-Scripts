#Dictionary Tool
#Let's see if I can make it work

listExample = []  #creates a list

with open("words.txt") as f:  #opens the "words" text file
    for line in f:
        listExample.append(line)

def search(WANTED_LENGTH):
    x = 0
    file = open("wow.txt","a+") #opens "wow" so I can save the right words to it

    while True:
        if x < len(listExample):
            word = listExample[x].strip() #removes spaces and \n
            if len(word) == WANTED_LENGTH: #this loop iterates through all words 
                lastLetter = word[-1]     #if the words is 11 letters long
                oneBeforeLetter = word[-2]
                threeBefore = word[-4]    #and this condition is met
                if lastLetter == oneBeforeLetter and lastLetter == threeBefore and lastLetter != word[-3]:
                    print("This word is cool!",word) #it prints it
                    word = word + "\n"   #adds a new line
                    file.write(word)     #and writes the word to the file "wow"
            x += 1 #iteration
        else:
            print("closing")
            file.close()
            break #breaks out if it is about to get an error
