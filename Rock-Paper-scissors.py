import random
import math

def win_check(player,opponent):
    if((player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r') ):
        return True
    return False

def play():
    computer=random.choice(['r','s','p'])
    user=' '
    while not(user=='p' or user=='r' or user=='s'):
        user=input("Choose 's'=scissor,'p'=paper, 'r'=rock : ").lower()
        # return user
    
    if user==computer:
        return(0,user,computer)
    elif win_check(user,computer):
        return(1,user,computer)
    else:
        return(-1,user,computer)


def playBestOf(n):
    computer_wins=0
    user_wins=0
    while n>0:
        result,user,computer=play()

        if result==0:
            print("User and computer both have chosen {} \n".format(user))
        elif result==1:
            user_wins+=1
            print("User has chosen {} and computer has chosen {}. Hence user WON this round! \n".format(user,computer))
        else:
            computer_wins+=1
            print("User has chosen {} and computer has chosen {}. Hence computer WON this round! \n".format(user,computer))

        n-=1

    if user_wins==computer_wins:
        print("Game is a TIE!")
    elif computer_wins>user_wins:
        print("Unfortunately! computer  WON! ")
    else:
        print("Congratulations User WON! What a CHAMP XD! ")

        
    
playBestOf(3)
while input("Play again? 'yes' or 'no' : ").lower()=='yes':
    playBestOf(3)




