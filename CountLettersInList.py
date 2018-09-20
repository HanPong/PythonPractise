import RandomCharacter
def main():
    #Create a list of characters
    chars=createList()
    #Display the list
    print("The lowercase letters are:")
    displayList(chars)
    #Count the occurences of the each letters
    counts=countLetters(chars)
    #Display counts
    print("The occurences of each letter are:")
    displayCounts(counts)

def createList():
    chars=[]
    for i in range(100):
        chars.append(RandomCharacter.getRandomLowerCaseLetter())
        #Return the list
        return chars

def displayList(chars):
    #Display the character in the list with 20 on each line
    for i in range(len(chars)):
        if(i+1)%20==0:
            print(char[i])
        else:
            print(char[i],end=' ')

def countLetters(chars):
    counts=26*[0]
    #For each lowercase letter in the list,count it
    for i in range(len(chars)):
        counts[ord(chars[i])-ord('a')]+=1
    return counts
#Display counts
def displayCounts(counts):
    for i in range(len(counts)):
        if(i+1)%10==0:
            print(counts[i],chr(i+ord('a')))
        else:
            print(counts[i],chr(i+ord('a')),end=' ')

main()