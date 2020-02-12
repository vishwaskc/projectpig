import random
import sys
import re
from comm import ComputerPlayer,HumanPlayer 

class Die:

    def __init__(self):
        self.value = random.randint(1, 6)

    def roll(self):

        self.value = random.randint(1, 6)
        if self.value == 1:
            raise RolledOneException

        return self.value


    def __str__(self):
        return "Rolled " + str(self.value) + "."


class Temp:

    def __init__(self):
        self.value = 0


    def reset(self):
        self.value = 0


    def add_dice_value(self, dice_value):
        self.value += dice_value


class RolledOneException(Exception):
    pass
        

class Game:
    def __init__(self, humans, computers):
        def check_pw():
            x=True
            while x:
                 if (len(password)<4 or len(password)>10):
                     print('length of password should be between 4 and 10')
                     break
                 elif not re.search('[a-z]',password):
                     print('password must contain atleast one alphabet')
                     break
                 elif not re.search('[A-Z]',password):
                     print('password must contain atleast one uppercase letter')
                     break
                 elif not re.search('[0-9]',password):
                     print('password must contain atleast one number')
                     break
                 elif not re.search('[$#@_&%!*]',password):
                     print('password must contain atleast one special character of $#@_&%!*')
                     break
                 elif re.search("\s",password):
                     print('space not allowed in password')
                     break
                 else:
                     print('password is valid')
                     return True
                     break
        self.players = []
        users ={}
        choice = ''
        if humans == 1:
            print()
            print('Player need to Register or Login')
            print()
            while choice !='e':
                
                choice = input("enter \n'r' to register \n'l' to login \n'e' to Exit :")
                if choice == 'r':
                    player_name = input('Enter name of human player: ')
                    password = input('Enter your password\n(Make sure it has at least 1 uppercase, 1 special char and 1 number)\n')
                    x=check_pw()
                    if player_name != '' and password != ''and x==True:
                        self.players.append(HumanPlayer(player_name))
                    
                    if player_name == '':
                        print('player name cannot be empty')
                        
                    elif password == '':
                        print('password cannot be empty')

                    elif x:
                        users[player_name] = password
                        print('you have registered successfully')
                        print('now you can login here')
                        login = input('enter your username\n')
                        if login in users:
                            pw = input('now enter your password\n')
                            if pw != password:
                                print('password not correct')
                            else:
                                print('you are logged in !')
                                print()
                                print('welcome "{}"!'.format(player_name))
                                print()
                                break
                        else:
                            print('username do not exist \nplease enter correct username or register')
                
                elif choice == 'e':
                    sys.exit(0)
                elif choice == 'l':
                   login = input('enter your username\n')
                   if login in users:
                       pw = input('now enter your password\n')
                       if pw != password:
                           print('password not correct')
                       else:
                           print('you are logged in!')
                           print()
                           print('welcome "{}"!'.format(player_name))
                           print()
                           break
                   else:
                       print('username do not exist \nplease enter correct username or register')
                    
            
                                
        else:
            for i in range(humans):
                print()
                print('PLAYER {} need to Register or Login'.format(i+1))
                print()
                while choice !='e':
                    choice = input("enter \n'r' to register \n'l' to login \n'e' to Exit :")
                    if choice == 'r':
                        player_name = input('Enter name of player no. {}: '.format(i+1))
                        password = input('enter your password\n(Your pw must have atleast 1 uppercase, 1 special char, 1 number)\n')
                        x=check_pw()
                        if player_name != '' and password != '' and x==True:
                             self.players.append(HumanPlayer(player_name))
                        
                        if player_name == '':
                             print('player name cannot be empty')
                             
                        elif password == '':
                            print('password cannot be empty')
                            

                        elif x:
                            users[player_name] = password
                            print('you have registered successfully')
                            print('now you can login here')
                            login = input('Enter your username\n')
                            if login in users:
                                pw = input('now enter your password\n')
                                if pw != password:
                                    print('password not correct')
                                else:
                                    print('you are logged in!')
                                    print()
                                    print('welcome "{}"!'.format(player_name))
                                    print()
                                    break
                            else:
                                print('username do not exist \nplease enter correct username or register ')
                                
                    elif choice == 'e':
                        sys.exit(0)
                    elif choice == 'l':
                         login = input('Enter your username\n')
                         if login in users:
                             pw = input('now enter your password\n')
                             if pw != password:
                                 print('password not correct')
                                 
                             else:
                                 print('you are logged in!')
                                 print()
                                 print('welcome "{}"!'.format(player_name))
                                 print()
                                 break
                         else:
                             print('username do not exist \nplease enter correct username or register')    

        for i in range(computers):
            self.players.append(ComputerPlayer(i))

        self.die = Die()
        self.temp = Temp()

    
    @staticmethod
    def welcome():

        print("*" * 70)
        print("Welcome to Pig Dice Game!" .center(70))
        print()

    def start(self):

        self.decide_first_player()

        while all(player.score < 100 for player in self.players):
            print('\nCurrent score is {}'.format(self.get_all_scores()))
            print('\n {} to play '.format(self.players[self.cur_player].name))
            self.temp.reset()

            while self.keep_rolling():
                pass

            self.players[self.cur_player].add_score(self.temp.value)
            self.next_player()

        ## The previous player has won...
        self.previous_player()
        print()
        print(' {} has won '.format(self.players[self.cur_player].name).center(70, '*'))
        print()
       
    def decide_first_player(self):

        self.cur_player = random.randint(1, 2) % 2

        print('{} starts'.format(self.players[self.cur_player].name))


    def next_player(self):
        
        self.cur_player = (self.cur_player + 1) % 2

    def previous_player(self):

        self.cur_player = (self.cur_player - 1) % 2


    def get_all_scores(self):

        return ', '.join(str(player) for player in self.players)


    def keep_rolling(self):
        
        try:
            roll = self.players[self.cur_player].keep_rolling(self.temp)
            if roll == True:
                dice_value = self.die.roll()
                self.temp.add_dice_value(dice_value)
                print('Rolled: {}, new temp value: {}'.format(dice_value, self.temp.value))
                return True
            else:
                return roll

        except RolledOneException:
            print('  Rolled one. Switching turns')
            self.temp.reset()
            return False


def main():
    Game.welcome()
    print('select the type of match you want to play')
    print()
    option = input('For QUICK MATCH press q \nFor CHALLENGE TOURNAMENT press c \npress e to Exit ')
    if option=='c':
        print()
        print('Match between TWO PLAYERS')
        human_players = 2
        computer_players=0
        game_obj = Game(human_players,computer_players)
    elif option=='q':
        print()
        print('Match between YOU and COMPUTER \n      Good Luck!     ')
        human_players=1
        computer_players=1
        game_obj = Game(human_players,computer_players)
    elif option=='e':
        print('Goodbye!')
        sys.exit(0)
    game_obj.start()

if __name__ == '__main__':
    main()




