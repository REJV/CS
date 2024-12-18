import random                                                                                   # import random
name = input("What is your name?")                                                              #print goodluck then the user name
print ("goodluck", name,"!")
wins = 0                                                                                        #establish vairables
rounds = 0

while True:                                                                                     #while the code is true (loop)
    number = random.randint(1, 10)                                                              #computer should generate random number 1-10
    guesses = 5                                                                                 #Guesses set to 5

    while guesses > 0:                                                                          #while guesses more than 0
        while True:                                                                             #while true loop
            try:                                                                                #try
                guess = int(input("Geuss a number one to ten"))                                 #imput the guess and convert to integer

                if guess >= 1 and guess <= 10:                                                  #if guess is more or equal to one and less or equal to ten
                    break                                                                       #break
                else:                                                                           #else
                    print('Pick a number between 1 and 10')                                     #print out please pick a number between 1 and 10
            except ValueError:                                                                  #except is their is a value error
                print("Please enter a number 1-10")                                             #then print please enter a number 1-10

        if guess == number:                                                                     #if guess = the number chosen
            wins += 1                                                                           #add one win
            print ("you won!")                                                                  #tell the user they won
            break                                                                               #break
        elif guess > number:                                                                    #if the number of the user guess is higher
            print ("The number is lower")                                                       #print the number is lower
        else:                                                                                   #else if the number the user guess is lower
            print ("The number is higher")                                                      #print that the number is higher
        guesses -= 1                                                                            #minus one guess 
    

    if guesses == 0:                                                                            #if guesses = 0
        print('You lost')                                                                       #print that you lost this round

    rounds += 1                                                                                 #round add one

    while True:                                                                                 #while loop
        again = input(f"You have won {wins} out of {rounds} rounds. Do you want to play again?")#give the score

        if (again == "yes"):                                                                    #do you want to play again (if answer is yes)
            break                                                                               #break
        elif (again == "no"):                                                                   #do you want to play again (if the answer is no)
        exit()                                                                                  #exit
        else:                                                                                   #else
            print ("type yes or no")                                                            #print type yes or no

    


