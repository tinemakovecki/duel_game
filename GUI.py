### THE USER INTERFACE
import tkinter
from tkinter import ttk
import Game
import Player

root = tkinter.Tk()
# TODO GET A NAME
root.title("Duel Game")

class GUI():

    # selecting window size by hand:
    # TODO flexible window
    Window_height = 300
    Window_width = 200

    def __init__(self, master):
        # creating the game window
        self.Game_window = tkinter.Frame(master, width=GUI.Window_width, height=GUI.Window_height)
        self.Game_window.pack()


        # TODO nicer buttons
        # creating the buttons for player 1
        # player 1 is at the bottom of the screen
        self.Player1_Button1 = tkinter.Button(self.Game_window, text="attack_1\n {}/{}".format("55", "70"),justify="right", command=self.attack1)
        # format(Game.Game.Player_1.Attack1.Damage, Game.Game.Player_1.Attack1.Hit_chance)
        self.Player1_Button1.grid(row=6, column=0, columnspan=2, rowspan=1)

        self.Player1_Button2 = tkinter.Button(self.Game_window, text="attack_2\n {}/{}".format("50", "80"),justify="right", command=self.attack2)
        self.Player1_Button2.grid(row=6, column=2, columnspan=2)

        self.Player1_Button3 = tkinter.Button(self.Game_window, text="attack_3\n {}/{}".format("45", "70"),justify="right", command=self.attack3)
        self.Player1_Button3.grid(row=7, column=0, columnspan=2)

        self.Player1_Button4 = tkinter.Button(self.Game_window, text="attack_4\n {}/{}".format("60", "60"),justify="right", command=self.attack4)
        self.Player1_Button4.grid(row=7, column=2, columnspan=2)


        # creating the buttons for player 2
        # player 2 is at the top of the screen
        self.Player2_Button1 = tkinter.Button(self.Game_window, text="attack_1\n {}/{}".format("70", "60"),justify="right", command=self.attack5)
        self.Player2_Button1.grid(row=0, column=0, columnspan=2)

        self.Player2_Button2 = tkinter.Button(self.Game_window, text="attack_2\n {}/{}".format("50", "80"),justify="right", command=self.attack6)
        self.Player2_Button2.grid(row=0, column=2, columnspan=2)

        self.Player2_Button3 = tkinter.Button(self.Game_window, text="attack_3\n {}/{}".format("50", "67"),justify="right", command=self.attack7)
        self.Player2_Button3.grid(row=1, column=0, columnspan=2)

        self.Player2_Button4 = tkinter.Button(self.Game_window, text="attack_4\n {}/{}".format("20", "80"),justify="right", command=self.attack8)
        self.Player2_Button4.grid(row=1, column=2, columnspan=2)


        # creating the health bars
        self.Player1_Health_Bar = ttk.Progressbar(self.Game_window, orient="horizontal", length=200, maximum=1000,
                                                  value=1000)
        self.Player1_Health_Bar.grid(row=5, column=1, columnspan=2)
        self.Player1_Health = 500

        self.Player2_Health_Bar = ttk.Progressbar(self.Game_window, orient="horizontal", length=200, maximum=500,
                                                  value=500)
        self.Player2_Health_Bar.grid(row=2, column=1, columnspan=2)
        self.Player2_Health = 500


        # creating the game image
        self.Game_picture = tkinter.Canvas(self.Game_window, background='white')
        self.Game_picture.grid(row=3, rowspan=2, column=0, columnspan=4)
        self.draw_game_picture() # have to put all image drawng in one function

        # setting background
        # TODO fitting background to canvas
        self.Background = tkinter.PhotoImage(file='background.png')
        self.Background_image = self.Game_picture.create_image(200, 200, image=self.Background)

        # inserting sprites
        self.Player1_sprite = tkinter.PhotoImage(file='Pikachu.png')
        self.Player1_sprite_image = self.Game_picture.create_image(GUI.Window_width, GUI.Window_height * 3 // 4,
                                                                   image=self.Player1_sprite)

        self.Player2_sprite = tkinter.PhotoImage(file='Charmander.png')
        self.Player2_sprite_image = self.Game_picture.create_image(GUI.Window_width, GUI.Window_height // 4,
                                                                   image=self.Player2_sprite)

        # TODO game menu
        # Main menu
        self.Menu = tkinter.Menu(master)
        master.config(menu=self.Menu)

        # Submenu
        self.Game_menu = tkinter.Menu(self.Menu)
        self.Menu.add_cascade(label="Game", menu=self.Game_menu)
        self.Game_menu.add_command(label="Quit", command=self.quit)
        self.Game_menu.add_command(label="New game", command=self.start_new_game(Player.Human(self), Player.Human(self)))
        # TODO add restart
        self.Game_menu.add_command(label="Help", command=self.help)


    def start_new_game(self, player1, player2):
        ''' starts a new game '''
        # create a new game
        self.Game = Game.Game()
        self.Player_1 = player1
        self.Player_2 = player2
        # start with player 1 turn
        self.Player_1.idle()


    def make_attack(self, selected_attack):
        ''' makes an attack and concludes a player turn '''
        (winner, hit_check, damage_dealt) = self.Game.take_turn(selected_attack)
        if winner == 'undefined' and hit_check == True:
            self.deal_damage(self.Game.Current_player, damage_dealt)
             # deals the damage to the current player, because current player switched after self.Game.take_turn ended

        elif winner == 'undefined':
            pass

        else:
            self.deal_damage(self.Game.return_opponent(), self.Game.return_opponent().HP)
            self.end_game()


    def end_game(self):
        ''' ends the game '''
        self.Game_picture.create_text(200, 150, font=("Purisa", 20), text='GAME OVER')

    # but why?
    def draw_game_picture(self):
        '''draws the image of the game'''
        # TODO
        # possible different images on attack/game modifiers

    # functions called by the buttons
    def attack1(self):
        self.make_attack(self.Game.Player1.Attack1)

    def attack2(self):
        self.make_attack(self.Game.Player1.Attack2)

    def attack3(self):
        self.make_attack(self.Game.Player1.Attack3)

    def attack4(self):
        self.make_attack(self.Game.Player1.Attack4)

    def attack5(self):
        self.make_attack(self.Game.Player2.Attack1)

    def attack6(self):
        self.make_attack(self.Game.Player2.Attack2)

    def attack7(self):
       self.make_attack(self.Game.Player2.Attack3)

    def attack8(self):
        self.make_attack(self.Game.Player2.Attack4)

    def quit(self):
        ''' closes the game window '''
        root.destroy()

    def help(self):
        #TODO
        pass

    def deal_damage(self, Victim, Damage_dealt):
        ''' shows the damage dealt to a character in the health bar '''
        if Victim == self.Game.Player1:
            self.Player1_Health -= Damage_dealt
            self.Player1_Health_Bar["value"] = self.Player1_Health
        elif Victim == self.Game.Player2:
            self.Player2_Health -= Damage_dealt
            self.Player2_Health_Bar["value"] = self.Player2_Health




# TODO window name,...
app = GUI(root)

root.mainloop()
