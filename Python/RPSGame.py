class RPSGame:
    def plyer_turns(self,name1,name2):
        user_input=""
        while(user_input.upper()!='N'):
            print(name1+"'s turn ")
            p1=input("Rock(R), Paper(P), Scissors(S): ")
            print(name2+"'s turn ")
            p2 = input("Rock(R), Paper(P), Scissors(S): ")
            if(
                (p1.upper()=='R' and p2.upper()=='S')or
                (p1.upper()=='S' and p2.upper()=='P')or
                (p1.upper()=='P' and p2.upper()=='R')
               ):
                print(name1,"WINS! ")
            elif(
                (p2.upper() == 'R' and p1.upper() == 'S') or
                (p2.upper() == 'S' and p1.upper() == 'P') or
                (p2.upper() == 'P' and p1.upper() == 'R')
                ):
                print(name2, "WINS! ")
            else:
                print("It's TIE ")
            user_input=input("Do you want to continue Y/N")
#Main function
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$WELCOME TO ROCK PAPER SCISORES GANE$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
p1_name = input("Enter 1st player name: ")
p2_name = input("Enter 2nd player name: ")
game_1=RPSGame()
game_1.plyer_turns(p1_name,p2_name)