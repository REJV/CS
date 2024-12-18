import random
wins = 0
botwins = 0
play = 1
score = 0
art = '''
                                ████          
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
'''
opponent =  ["Rock", "Paper", "Scissors"]
print ("first to three Wins! When you lose a round you lose one score!")

while (play == 1):
    answer = str.lower(input("Rock, Paper or Scissors?"))
    eanswer = random.choice(opponent)
    print ("you pick", answer)
    print ("computer picked", eanswer)
    if (answer == "rock"):
        if (eanswer == "Rock"):
            print ("you tied") 
        elif (eanswer == "Paper"):
            print ("you lost")
            score -= 1
        else:
            print ("you won")
            score += 1
    elif (answer == "paper"):
        if (eanswer == "Paper"):
            print ("you tied")
        elif (eanswer == "Scissors"):
            print ("you lost")
            score -= 1
        else:
            print ("you won")   
            score += 1
    elif (answer == "scissors"):
        if (eanswer == "Scissors"):
            print ("you tied")
        elif (eanswer == "Rock"):
            print ("you lost")
            score -= 1
        else:
            print ("you won")
            score += 1
    else:
        print ("Please only say Rock, Paper or Scissors")
    print ("Your score is", score,"!")
    if (score == 3):
        print ("You WIN the game!!!!!!!!!")
        wins += 1
    elif (score == -3):
        print ("You LOSE the game!!!!!!!!!")
        botwins += 1
    if (score == 3 or score == -3):
        again = str.lower(input("Do you want to play again? (yes or no)"))
        if (again == "yes"):
           print ("you have",wins,"wins!, Computer has", botwins, "wins!")
           score = 0
        elif (again == "no"):
            print (art,"\n", "Good game!\n","you have",wins,"wins!, Computer has", botwins, "wins!")
            play = 0
        else:
            print ("Please answer yes or no!")