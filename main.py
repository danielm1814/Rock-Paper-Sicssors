from random import randint
import time

ties = 0
computer_wins =0
user_wins=0

def check_winner(user, comp):
    dic = {0:"Rock", 1:"Paper", 2:"Scissors"}
    time.sleep(1)
    print("User did " + dic[user])
    time.sleep(1)
    print("Computer did " + dic[comp])
    time.sleep(1)
    global ties
    global computer_wins
    global user_wins
    if (user == comp):
        print("It was a tie!")
        ties += 1
    elif (user == 0):
        if(comp == 1):
            print("The Computer Won")
            computer_wins += 1
        else:
            print("The Player Won")
            user_wins += 1
    elif (user == 1):
        if(comp == 2):
            print("The Computer Won")
            computer_wins += 1
        else:
            print("The Player Won")
            user_wins += 1
    else:
        if(comp == 0):
            print("The Computer Won")
            computer_wins += 1
        else:
            print("The Player Won")
            user_wins += 1

def main():
    
    ask = input("Would you like to play rock, paper, scissors?\n")
    if (ask.lower() == "no"):
        print("Have a good day!")
    else:
        while(True):
            print("Rock")
            time.sleep(1)
            print("Paper")
            time.sleep(1)
            print("Scissor")
            time.sleep(1)
            print("Shoot!")
            user_move = input("Pick a number 0=Rock, 1=Paper, 2=Scissors\n")
            acceptable_moves = ["0", "1", "2"]
            while (user_move not in acceptable_moves):
                user_move = input("Pick a number 0=Rock, 1=Paper, 2=Scissors\n")
            user_move = int(user_move)
            comp_move = randint(0,2)
            check_winner(user_move, comp_move)
            time.sleep(1)
            print("Scoreboard:")
            print("Wins: " + str(user_wins))
            print("Loses: " + str(computer_wins))
            print("Ties: " + str(ties))
            continues = input("Would you like to keep playing?\n")
            if (continues.lower() == "no"):
                break
        print("That was some good rock, paper, scissors!")


main()
