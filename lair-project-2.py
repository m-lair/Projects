


import random           # import Random Library



# Print out directions for game
print("welcome to rock, paper, scissors, lizard, spock")        
print("")
print("lizard beats paper and spock and is beaten by rock, and spock beats"
      "scissors and rock but is beaten by paper,")
print("")



 



def Name(num):                   # Assign a constant to each number 
        if num == 0:
            result = "ROCK"      # Function allows for easier readability for user
        elif num == 1:
            result = "PAPER"
        elif num == 2:
            result = "SCISSORS"
        elif num == 3:
            result = "LIZARD"
        else:
            result = "SPOCK"
        return result

       # Loop to allow the user the choice to play





win = 0         # Number of wins set to 0 
lose = 0        # Number of loses set to 0
play = "y"      # Set loop variable to "Y" to start loop
playcount = 0
user_play = 1



while playcount < user_play:    # loop until desired amount of rounds is reached

        

        print("")

        computer = random.randint(0,4) # gets choice for user and computer weapons
        user = int(input("choose Rock(0), Paper(1), Scissors(2), Lizard(3) or Spock(4): "))

        # all outputs for different outcomes 
        if user == 0:
                if computer == 2 or computer == 3:
                        print("YOU WIN!")
                        print("Player chose", Name(user), "computer chose", Name(computer))
                        win += 1
                        playcount += 1
                elif user == computer:
                        playcount += 1
                        print("it's a draw!")
                else:
                        lose += 1
                        playcount += 1
                        print("YOU LOSE")
                        print("Player chose ", Name(user), "computer chose ", Name(computer))


                                        # End if


        if user == 1:
                if computer == 0 or computer == 4:
                        print("YOU WIN!")
                        print("Player chose", Name(user), "computer chose", Name(computer))
                        win += 1
                        playcount += 1
                elif user == computer:
                        playcount += 1
                        print("it's a draw!")
                else:
                        lose += 1
                        playcount += 1
                        print("YOU LOSE")
                        print("Player chose", Name(user), "computer chose", Name(computer))


                                        # End if

        if user == 2:
                if computer == 1 or computer == 3:
                        print("YOU WIN!")
                        print("Player chose", Name(user), "computer chose", Name(computer))
                        win +=1
                        playcount += 1
                elif user == computer:
                        playcount += 1
                        print("it's a draw!")
                else:
                        lose += 1
                        playcount += 1
                        print("YOU LOSE")
                        print("Player chose", Name(user), "computer chose", Name(computer))


                                        # End if
                                              
        if user == 3:
                if computer == 4 or computer == 2:
                        print("YOU WIN!")
                        print("Player chose", Name(user), "computer chose", Name(computer))
                        win += 1
                        playcount += 1
                elif user == computer:
                        playcount += 1
                        print("it's a draw!")
                else:
                        lose += 1
                        playcount += 1
                        print("YOU LOSE")
                        print("Player chose", Name(user), "computer chose", Name(computer))



                                        # End if

        if user == 4:
                if computer == 0 or computer == 2:
                        print("YOU WIN!")
                        print("player chose", Name(user), "computer chose", Name(computer))
                        win += 1
                        playcount += 1
                elif user == computer:
                        playcount += 1
                        print("it's a draw!")
                else:
                        lose += 1
                        playcount += 1
                        print("YOU LOSE")
                        print("Player chose", Name(user), "computer chose", Name(computer))
                
                                        # End if
        
        if play == "Y" or play == "y":
         # Choice to loop again
                play = (input("Would you like to play again, (Y)es or (N)o: "))

                user_play = (int(input("How many times would you like to play again: ")))
                play = "N"
                user_play += 1

                
        
                

          



# present scores once loop is broken
print("")
print("You won", win,"times and lost", lose, "times")




    
    
                
                

