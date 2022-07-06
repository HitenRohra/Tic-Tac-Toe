import random
#------------GLOBAL VARIABLES------------

board=["-","-","-",
        "-","-","-",
        "-","-","-",]

winner=0   # 0 = winner not declared , 1 = user, 2 = comp 

#----------FUNCTIONS--------------

def display():
    print(board[0] + " | " + board[1] + " | " + board[2] )
    print(board[3] + " | " + board[4] + " | " + board[5] )
    print(board[6] + " | " + board[7] + " | " + board[8] )

def play():
    display()                           # Display Initial Board
    while '-' in board and winner == 0 :  # Until Board spaces are empty or winner is declared !
        handle_turn()
        comp_turn()
        display()
        checkwin()
    
    #Game ends here
    if winner==0:
        print("It was a TIE! Better luck next time! ")
    elif winner==1:
        print("User Wins! Congratulations! ")
    elif winner==2:
        print("Computer Wins! Better luck next time! ")

def handle_turn():
    position = int(input("Please choose a position from 1 to 9: ")) 
    position-=1
    if checkempty(position)==True:  
        board[position]='X'
    else:                           #Loop until valid choice is entered
        print("Please enter a valid choice! "+"\n")
        handle_turn()

def comp_turn():
    comp_choice=random.randint(0,8)
    if checkempty(comp_choice)==True:
        board[comp_choice]='O'
    else:
        comp_choice=random.randint(0,9)
        comp_turn()

def checkwin():
    global winner
    for i in range(0,9,3):          # Checling Row winner
        if (board[i]==board[i+1]==board[i+2]!='-'):
            if board[i] == 'X':
                winner=1
            else:
                winner=2
    for i in range(0,3):             #Check Column Winner
        if (board[i]==board[i+3]==board[i+6] and board[i]!='-'):
            if board[i] == 'X':
                winner=1
            else:
                winner=2

    #Check Diagonal Winner
    if (board[0]==board[4]==board[8]and board[0]!='-'):
        if board[0] == 'X':
            winner=1
        else:
            winner=2
    if (board[2]==board[4]==board[6]and board[2]!='-'):
        if board[2] == 'X':
            winner=1
        else:
            winner=2


def checkempty(num):
    if (num >-1 and num < 10) and (board[num]=='-'):
        return True
    else:
        return False

choice="Y"
while choice=="Y":
    board=["-","-","-",
        "-","-","-",
        "-","-","-",]
    winner = 0 
    play()
    choice=input("Do you want to play again? (Y/N) ").upper()