import random                                                                                       #imports random
wins = 0                                                                                            #Makes vairable wins = 0
botwins = 0                                                                                         #Makes vairable botwins = 0
play = 1                                                                                            #Makes vairable play = 1
score = 0                                                                                           #Makes vairable score = 0
art = '''                                                                                       
                                ██  ██ 
                              ▓▓    ██ 
                              ▓▓    ██ 
                            ██    ██
                            ██    ██
                          ██      ██ 
                          ██    ██ 
  ██████████            ██      ██ 
██░░▒▒▒▒░░▒▒██    ██████        ██████████████
██░░░░░░░░▒▒██  ██                          ██
██▒▒▒▒▒▒░░▒▒██  ██                          ██
██▓▓▓▓▓▓▓▓▓▓██  ██                ██████████
██▓▓▓▓▒▒▓▓▓▓██  ██                        ██
██▓▓▓▓▒▒▒▒▒▒██  ▓▓                ░░░░    ██
██▓▓▓▓▓▓▓▓▓▓██  ██                ████████    
██▓▓▓▓▓▓▓▓▓▓██  ██                      ██
██▓▓▓▓▓▓▓▓▓▓██  ██                      ██
██▓▓▓▓▓▓▓▓▓▓██  ██                ██████
██▓▓▓▓▓▓  ▓▓██  ██                    ██
██▓▓▓▓▓▓▓▓▓▓██    ████████████████████
  ██████████                      
'''                                                                                                 #Makes vairable art = image above
opponent =  ["Rock", "Paper", "Scissors"]                                                           #Makes a list of weapons for oppenonent to pick
print ("first to three Wins! When you lose a round you lose one score!")                            #Prints the basic of the game

while (play == 1):                                                                                  #Ensures that game only wants to start when user wants to play
    answer = str.lower(input("Rock, Paper or Scissors?"))                                           #Ask user for imput on their weapon
    eanswer = random.choice(opponent)                                                               #Generates random weapon from opponents list
    print ("you pick", answer)                                                                      #Prints users input
    print ("computer picked", eanswer)                                                              #Prints computers random input
    if (answer == "rock"):                                                                          # If answer = rock then
        if (eanswer == "Rock"):                                                                     # If eanswer = rock then
            print ("you tied")                                                                      # Tells user they tied
        elif (eanswer == "Paper"):                                                                  # If eanswer = paper then
            print ("you lost")                                                                      # Tells user they lost
            score -= 1                                                                              #Lowers score because user lost
        else:                                                                                       #Else then do 
            print ("you won")                                                                       #Tells user they won
            score += 1                                                                              #Adds one score because user won
    elif (answer == "paper"):                                                                       # If answer = paper then
        if (eanswer == "Paper"):                                                                    # If eanswer = paper then
            print ("you tied")                                                                      # Tells user they tied
        elif (eanswer == "Scissors"):                                                               # If eanswer = scissors then
            print ("you lost")                                                                      # Tells user they lost
            score -= 1                                                                              #Lowers score because user lost
        else:                                                                                       #Else then do 
            print ("you won")                                                                       # Tells user they won
            score += 1                                                                              #Adds one score because user won
    elif (answer == "scissors"):                                                                    # If answer = scissors then
        if (eanswer == "Scissors"):                                                                 # If eanswer = scissors then
            print ("you tied")                                                                      # tells user they tied
        elif (eanswer == "Rock"):                                                                   # If eanswer = rock then
            print ("you lost")                                                                      # Tells user they lost
            score -= 1                                                                              #Lowers score because user lost
        else:                                                                                       #Else then do 
            print ("you won")                                                                       #T ells user they won
            score += 1                                                                              #Adds one score because user won
    else:                                                                                           #Else then do 
        print ("Please only say Rock, Paper or Scissors")                                           #If user dosen't answer with rock paper or scissors then tells them to repeat
    print ("Your score is", score,"!")                                                              #Prints score at end of each round
    if (score == 3):                                                                                #If score = 3 then you win
        print ("You WIN the game!!!!!!!!!")                                                         #Tells user they won
        wins += 1                                                                                   #Adds one win to the user
    elif (score == -3):                                                                             #If score = -3 then you lost
        print ("You LOSE the game!!!!!!!!!")                                                        #Tells user they lost the game
        botwins += 1                                                                                #Gives the computer a win
    if (score == 3 or score == -3):                                                                 #Once someone wins prompts user for imput if they want to play again
        again = str.lower(input("Do you want to play again? (yes or no)"))                          #Promts user for input
        if (again == "yes"):                                                                        #If user = yes to wanting to play again
           print ("you have",wins,"wins!, Computer has", botwins, "wins!")                          #Tells them how many wins computer and player have
           score = 0                                                                                #Resets user score to 0
        elif (again == "no"):                                                                       #If player dosent want to play again
            print (art,"\n", "Good game!\n","you have",wins,"wins!, Computer has", botwins, "wins!")#Prints art, says good games, and says both user and computer wins.
            play = 0                                                                                #Sets play to 0 which dosen't allow the game to repeat itself
        else:                                                                                       #IF user answers with something other than yes or no
            print ("Please answer yes or no!")                                                      #promts user to repeat with either yes or no