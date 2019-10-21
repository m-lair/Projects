

import random

def displayRules():
    ''' displays the rules of craps.

        input: none

        returns: none
    '''
    print("Welcome to Craps! Here is how you play.")
    print("You will roll two dice and if on your first roll you get a sum",
          "of 7 or 11 you win! Although, if you roll a 2, 3, or 12 you lose",
          "if you roll none of these then the number you rolled becomes you point",
          "you must then keep rolling to you roll your point again or a 7",
          "if you roll a 7 you lose. If you roll your point you win!")

def getStartingBalance():
    ''' Gets users starting balance for game

        input: none

        returns: bank balance 
    '''
    balance = eval(input("What is your total bankroll: "))
    return balance

def getWager():
    '''gets users wager for roll

       input: none

       returns: wager
    '''
    wager = eval(input("How much would you like to bet: "))
    wager += .00
    return wager
    
        
def isValidWager(wager, balance):
    '''computes if the wager is able to be placed

       input: wager, balance

       returns: True or False
    '''
    if wager < balance:
        return True
    elif wager > balance:
        return False

def rollDie():
    '''generates random integer between 1 and 6 inlcusive

       input: none

       returns: random integer
    '''
    die = random.randint(1,6)
    return die

def sumDice(die1, die2):
    ''' Adds two values together

        input: die1 and die2

        returnt integer between 1-12
    '''
    sumDice = die1 + die2
    return sumDice

def isWinOrLossOrPoint(sumDice):
    '''calcualtes if the sum of the dice is a win, loss, or point in the rules of Craps

       input: sumDice

       returns: strings "win", "lose", and "point"
    '''
    if sumDice == 7 or sumDice == 11:
        return "Win"
    elif sumDice == 2 or sumDice == 3 or sumDice == 12:
        return "Loss"
    else:
        return "point"

def isPointOrLossOrNeither(sumOfDice, pointValue):
    '''decideds if the rolls after making the "point" is a win or a loss

       input: sumOfDice, pointValue

       returns: string value of "Loss", "Win", "Neither"
    '''
    if sumOfDice == 7:
        return "Loss"
    elif sumOfDice == pointValue:
        return "Win"
    else:
        return "Neither"
    


def main():
    '''runs the main game loop

       input: none

       returns: none
    '''
    displayRules()                  # displays rules for players 
    print()
    balance = getStartingBalance()  # get starting balance
    play = "Y"                      # prime the While loop to start
    
    
    while play == "Y" or play == "y":



        wager = getWager()                              # place wager in variable
        while isValidWager(wager, balance) == False:    # loop to make sure wager is valid

            print("That is not a valid wager, please enter again")
            wager = getWager()
            
        
            

        
        print()
        input("Press ENTER to roll the dice") 
        die1 = rollDie()                            # get first random die
        die2 = rollDie()                            # get second random die
        dice = sumDice(die1, die2)                  # get the sum of die
        print("you rolled", dice)
        if isWinOrLossOrPoint(dice) == "Win":       # Win on first role if
            print("You win!")
            balance = balance + wager               # add wager back to balance for winning
            print("Your balance is now $", balance)
           
        elif isWinOrLossOrPoint(dice) == "Loss":    # lose on first roll if
            print("You Lose!")
            balance -= wager                        # subtract wager from balance for loss
            print("Your balance is now $", balance)
           
                
            
            
        else:
            print("your point is", dice)            # if for establishing the point
            point = dice
            input("press ENTER to roll the dice")    
            die1 = rollDie()
            die2 = rollDie()
            dice = sumDice(die1, die2)
            print("You rolled", dice)
            
            while isPointOrLossOrNeither(dice, point) == "Neither": # re-roll till win or loss 
                input("press ENTER to roll the dice")               
                die1 = rollDie()
                die2 = rollDie()
                dice = sumDice(die1, die2)
                print("You rolled", dice)
                
            if isPointOrLossOrNeither(dice, point) == "Loss":       # if for loss after first roll
                print("You lose")
                balance -= wager
                print("your balance is now $", balance)
                
                
            elif isPointOrLossOrNeither(dice, point) == "Win":      # if for winning after first roll
                print("You Win!")
                balance += wager
                print("your balance is now $", balance)

        play = input("Would you like to play again Y/N: ")          # present user the choice to play again
        

    print("Goodbye!")
            
            
            

        

        
        







main()
        
        
        
    
    

    
