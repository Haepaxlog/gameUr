import dice,time
from getkey import getkey,keys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Spielstein():
    def __init__(self,Player,mov_pw):
        self.Player = Player
        self.mov_pw = mov_pw
    def check_mov(self):
        if self.Player == "Player1":
            self.activePl = "Stein1"
            self.nonactivePl = "Stein2"
            self.movs_set = movs_l
        elif self.Player == "Player2":
            self.activePl = "Stein2"
            self.nonactivePl = "Stein1"
            self.movs_set = movs_r
    def side(self,Goal_l,Goal_r,Spielstein_count_l,Spielstein_count_r):
        self.check_mov()

        def loop_through():
            self.opt_list = []
            for x in self.movs_set:
                if self.movs_set[x] == self.activePl:
                    self.opt_list.append(x)
            for x in movs_mid:
                if movs_mid[x] == self.activePl:
                    self.opt_list.append(x)
            print(f"You can move Stones at postion {self.opt_list}")
    
        def from_which_set(choice):
            if choice <5 or choice >12:
                if self.activePl == "Stein1":
                    if movs_l[choice] != "none":
                        return movs_l
                elif self.activePl =="Stein2":
                    if movs_r[choice] != "none":
                        return movs_r
            else:
                if movs_mid[choice] != "none":
                    return movs_mid
        
        #TEST! -> passed if f is referenced outside function
        def logic_func_place(movs_Pl):
            if mov_pw <= 4:
                if movs_Pl[self.mov_pw] != self.activePl:
                    movs_Pl[self.mov_pw] = self.activePl
            elif mov_pw > 4:
                if movs_mid[self.mov_pw] != self.activePl:
                    movs_mid[self.mov_pw] = self.activePl
            else:
                print("You can't set a new piece here")
        
        #TEST! -> passed
        def logic_func(choice,mov,movs_Pl,Goal_Pl,Spielstein_count_Pl):
            if mov <= 4:
                if movs_Pl[mov] != self.activePl:
                    movs_Pl[mov] = self.activePl
                    movs_Pl[choice] = "none"
                else:
                    f = True
                    return f
            if mov >=5  and mov <=12:
                if  movs_mid[mov] != self.activePl:
                    movs_mid[mov] = self.activePl
                elif movs_mid[mov] == self.nonactivePl:
                    movs_mid[mov] = self.activePl
                    Spielstein_count_r += 1
                from_which_set(choice)[choice] = "none"
            if mov >12 and mov <= 14:
                if movs_Pl[mov] != self.activePl:
                    movs_Pl[mov] = self.activePl
                if movs_mid[choice] == self.activePl:
                    movs_mid[choice] ="none"
                if movs_Pl[choice] == self.activePl:
                    movs_Pl[choice] = "none"
                else:
                    f = True
                    return f
            if mov >= 15:
                if choice in movs_mid:
                    movs_mid[choice] = "none"
                elif choice in movs_Pl:
                    movs_Pl[choice] = "none"
                Goal_Pl += 1
                print(f"aktuelle Punktzahl: {Goal_Pl}")
            Spielstein_count_Pl -= 1
            

    
        if self.activePl == "Stein1":
            f = True
            while f == True:
                print()
                show_board()
                print("Do you want to take a new piece (n) or continue (c) moving? ")
                mov_want = getkey()
                if mov_want == "n":
                    f = False
                    logic_func_place(movs_l)
                if mov_want == "c":
                    loop_through()
                    choice = int(input("What position do you want to move "))
                    if choice in self.opt_list:
                        f = False
                        mov = choice + mov_pw
                        logic_func(choice,mov,movs_l,Goal_l,Spielstein_count_l)
        elif self.activePl == "Stein2":
            f = True
            while f == True:
                print()
                show_board()
                print("Do you want to take a new piece (n) or continue (c) moving? ")
                mov_want = getkey()
                if mov_want == "n":
                    f = False
                    logic_func_place(movs_r)
                if mov_want == "c":
                    loop_through()
                    choice = int(input("What position do you want to move "))
                    if choice in self.opt_list:
                        f = False
                        mov = choice + mov_pw
                        logic_func(choice,mov,movs_r,Goal_r,Spielstein_count_r)

def steps_point():
    print("\n")
    print(f"{bcolors.WARNING}{Player}{bcolors.ENDC} is going to throw the dice")
    print("Enter Spacebar to throw dice")
    key_start = getkey()
    if key_start == keys.SPACE:
        global mov_pw 
        global turn
        mov_pw = dice.dice_throw()
        if mov_pw == 0:
            print(f"{mov_pw}: Your turn is over")
            turn = False 
        else:    
            if mov_pw == 1:
                print(f"You can move {bcolors.OKBLUE}{mov_pw}{bcolors.ENDC} step")
                turn = True
            else:
                print(f"You can move {bcolors.OKBLUE}{mov_pw}{bcolors.ENDC} steps")
                turn = True
        time.sleep(1)
    return mov_pw, turn 

def show_board():
    print("\n")
    l_val = list(movs_l.values())
    r_val = list(movs_r.values())
    mid_val = list(movs_mid.values())
    x = 0
    for i in reversed(range(0,4)):
        print(f"{l_val[i]:8} {mid_val[x]:8} {r_val[i]:8}")
        x += 1
    for i in range(4,6):
        print(f"{mid_val[i]:^22} ")
    x = 6
    for i in reversed(range(6,8)):
        print(f"{l_val[i-2]:8} {mid_val[x]:8} {r_val[i-2]:8}") 
        x += 1
    
def title_screen():
    print("-"*24)
    print("| THE ROYAL GAME OF UR |")
    print("-"*24)

#shows title screen
title_screen()
print("\n" *5)

print("Press X to start")
key = getkey()
if key == "x":
    print()
    #Playername input
    f = False
    while f==False:
        try:
            Player1,Player2  = input("Enter 2 player names (seperated by space): ").split()
            f = True 
        except:
            f = False
         
print()

Playerbg = ["Player1","Player2"]
#Selecting Beginner
print("Throwing dice to determine beginner")
print("\n" *3)
time.sleep(2)
beg1 = dice.dice_throw()
beg2 = dice.dice_throw()
while beg1==beg2:
    beg1 = dice.dice_throw()
    beg2 = dice.dice_throw()
if beg1 > beg2:
    print(f"{beg1} was {Player1}'s throw, {Player2}'s {beg2} was lower")
    print(f"{Player1} will begin")
    print()
    Player = Playerbg[0]
else:
    print(f"{beg2} was {Player2}'s throw, {Player1}'s {beg1} was lower")
    print()
    print(f"{Player2} will begin")
    print()
    Player = Playerbg[1]

print()
#initialising  Values
movs_l = {1: "none", 2: "none", 3: "none", 4: "none",13: "none", 14: "none"}
movs_r = {1: "none", 2: "none", 3: "none", 4: "none",13: "none", 14: "none"}
movs_mid = {5: "none", 6: "none", 7: "none", 8: "none", 9: "none", 10: "none", 11: "none", 12: "none"}

Goal_l = 0
Goal_r = 0
Spielstein_count_l = 7
Spielstein_count_r = 7

show_board()
time.sleep(1)
#initialiser of game
steps_point()
Play = Spielstein(Player,mov_pw)
if turn == True:
    Play.side(Goal_l,Goal_r,Spielstein_count_l,Spielstein_count_r)
show_board()
#game loop
while Goal_l <= 7 or Goal_r <= 7:
    f = 1
    if Player == "Player1":
        Player = "Player2"
    elif Player == "Player2":
        Player = "Player1"
    steps_point()
    if turn == False:
        f = 2
    if f == 1:
        Play = Spielstein(Player,mov_pw)
        Play.side(Goal_l,Goal_r,Spielstein_count_l,Spielstein_count_r)
        show_board()
        

if Goal_l == 7:
    print(f"{Player1} gewinnt")
elif Goal_r ==7:
    print(f"{Player2} gewinnt")



    





