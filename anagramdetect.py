import string
def anagramDetect(stringA ,stringB ):
    tempA = stringA
    tempB = stringB
    #maniupulate strings to remove spaces, capitalizations, punctuations
    tempA = tempA.replace(' ','')
    tempB = tempB.replace(' ','')
    tempA = tempA.lower()
    tempB = tempB.lower()
    for c in string.punctuation:
        tempA = tempA.replace(c,'')
    for c in string.punctuation:
        tempB = tempB.replace(c,'')
    tempAA = sorted(tempA)
    tempBB = sorted(tempB)
    if (tempAA == tempBB):
        print stringA + " is an anagaram of " + stringB
    else:
        print stringA + " is NOT an anagaram of " + stringB



def main():
    anagramDetect("wisdom", "mid sow")
    anagramDetect("Seth Rogan" , "Gathers No")
    anagramDetect("Reddit" , "Eat Dirt")
    anagramDetect("Schoolmaster" , "The classroom")
    anagramDetect("Astronomers" , "Moon starer")
    anagramDetect("Vacation Times" , "I'm Not as Active")
    anagramDetect("Dormitory" , "Dirty Rooms")


if __name__ == '__main__':
    main()
