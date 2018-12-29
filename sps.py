'''ROCK PAPER SCISSOR'''
'''
1 = Rock
2 = Paper
3 = Scissor
'''

import random
import os

def result(player, comp):
    if(player==1):
        if(comp==2):
            return 2
        elif(comp==3):
            return 1
    elif(player==2):
        if(comp==1):
            return 1
        elif(comp==3):
            return 2
    elif(player==3):
        if(comp==2):
            return 1
        elif(comp==1):
            return 2

print("\t\t\t##########################")
print("\t\t\t##                      ##")
print("\t\t\t## ROCK, PAPER, SCISSOR ##")
print("\t\t\t##                      ##")
print("\t\t\t##########################")

print("\n\n:::::RULES:::::")
print("1. ROCK beats SCISSOR")
print("2. PAPER beats ROCK")
print("3. SCISSOR bests PAPER")


pname=input("Enter player name: ").upper()
os.system("cls")

pscore=0
cscore=0
choice='y'
rounds=1

while(choice=='y' or choice=='Y'):
    print("\t\t\t##########################")
    print("\t\t\t##                      ##")
    print("\t\t\t## ROCK, PAPER, SCISSOR ##")
    print("\t\t\t##                      ##")
    print("\t\t\t##########################")
    print("Options: ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")

    print("ROUND "+str(rounds))
    player=int(input("enter your input: "))
    if(player<1 or player>3):
        player=int(input("enter valid input: "))
    comp=random.randint(1,3)
    print("\n"+pname+"="+str(player))
    print("computer="+str(comp))
    res=0

    if(player==comp):
        print("--------TIE--------")
    res=result(player,comp)

    if(res==1):
        print("\n#####"+pname+" wins#####")
        pscore=pscore+1
    elif(res==2):
        print("\n#####COMPUTER wins#####")
        cscore=cscore+1
    
    print("\n\n#####SCORE BOARD#####")
    print(pname+"="+str(pscore))
    print("Computer="+str(cscore))
    choice=input("Want to play again:(Y/N) ")
    os.system("cls")
    if(choice=='y' or choice=='Y'):
        rounds=rounds+1

os.system("cls")
print("\t\t\t##########################")
print("\t\t\t##                      ##")
print("\t\t\t## ROCK, PAPER, SCISSOR ##")
print("\t\t\t##                      ##")
print("\t\t\t##########################")

print("FINAL SCORE")
print(pname+"="+str(pscore))
print("Computer="+str(cscore))
if(pscore<cscore):
    print("\n\t\tCOMPUTER WINS")
elif(pscore>cscore):
    print("\n\t\t"+pname+" WINS")
else:
    print("\n\t\tTIE\n\tBOTH ARE WINNERS")