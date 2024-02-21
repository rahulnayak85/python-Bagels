

#get an initial guess from the user
# count the number of attempts that the user is making



#create a random 3 digit number (in secret)
def getSecretNum():
    from random import randint
    secret = randint(100,999)
    secretStr = str(secret)
    return secretStr

#get answer to display to user
def getAnswer(guessNum, secretNum):
    answer = []
    for i in range (0,3):
        if guessNum[i] == secretNum[i] :
            answer.append("Fermi")
        elif guessNum[i] in secretNum :
            answer.append("Pico")
    if len(answer) == 0:
        return 'Bagels'
    else:
        answer.sort()
        return ' '.join(answer)

#give all the initial info to the user


def main():
    maxGuesses = 3
    print("Guessing game")
    secretNum = getSecretNum()
    print("I have thought up a number")
    print("You have 3 guesses to get it")
    numGuesses = 1
    while numGuesses < 4:
        guess = str(int(input("Enter your 3 digit guess")))
        answer = getAnswer(guess, secretNum)
        print(answer)
        numGuesses += 1

        if guess == secretNum:
            print("You got it!")
        if numGuesses > maxGuesses:
            print("You ran out of guesses")
            print(f"The answer was {secretNum}")

if __name__ == '__main__':
    main()