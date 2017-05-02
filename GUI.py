####### - MAIN GAME FILE & USER INTERFACE - #######

import tkinter
from tkinter import ttk
import Game
import Player

root = tkinter.Tk()
root.title("Duel Game")

class GUI():

    # TODO select/stretchable
    Window_height = 300
    Window_width = 200

    def __init__(self, master):
        # window
        self.Game_window = tkinter.Frame(master, width=GUI.Window_width, height=GUI.Window_height)
        self.Game_window.pack()

        # Main menu
        self.Main_menu = tkinter.Menu(master)
        master.config(menu=self.Main_menu)

        # Submenu
        self.Game_options_menu = tkinter.Menu(self.Main_menu)
        self.Main_menu.add_cascade(label="Game", menu=self.Game_options_menu)
        self.Game_options_menu.add_command(label="Quit", command=self.quit)
        self.Game_options_menu.add_command(label="New game",
                                           command=self.start_new_game(Player.Human(self), Player.Human(self)))
        # TODO add restart/change 'New Game'
        self.Game_options_menu.add_command(label="Help", command=self.help)


        # buttons
        # player 1 is at the bottom
        self.Player1_button1 = tkinter.Button(self.Game_window,
                                              text="attack_1\n {}/{}".format(
                                                  self.Game.Player1.Attack1.Damage,
                                                  self.Game.Player1.Attack1.Hit_chance),
                                              justify="right", command=lambda: self.select_attack_for_player1(1))
        self.Player1_button1.grid(row=6, column=0, columnspan=2, rowspan=1)

        self.Player1_button2 = tkinter.Button(self.Game_window,
                                              text="attack_2\n {}/{}".format(
                                                  self.Game.Player1.Attack2.Damage,
                                                  self.Game.Player1.Attack2.Hit_chance),
                                              justify="right", command=lambda: self.select_attack_for_player1(2))
        self.Player1_button2.grid(row=6, column=2, columnspan=2)

        self.Player1_button3 = tkinter.Button(self.Game_window,
                                              text="attack_3\n {}/{}".format(
                                                  self.Game.Player1.Attack3.Damage,
                                                  self.Game.Player1.Attack3.Hit_chance),
                                              justify="right", command=lambda: self.select_attack_for_player1(3))
        self.Player1_button3.grid(row=7, column=0, columnspan=2)

        self.Player1_button4 = tkinter.Button(self.Game_window,
                                              text="attack_4\n {}/{}".format(
                                                  self.Game.Player1.Attack4.Damage,
                                                  self.Game.Player1.Attack4.Hit_chance),
                                              justify="right", command=lambda: self.select_attack_for_player1(4))
        self.Player1_button4.grid(row=7, column=2, columnspan=2)


        # player 2 is at the top
        self.Player2_button1 = tkinter.Button(self.Game_window,
                                              text="attack_1\n {}/{}".format(
                                                  self.Game.Player2.Attack1.Damage,
                                                  self.Game.Player2.Attack1.Hit_chance),
                                              justify="right", command=lambda: self.select_attack_for_player2(1))
        self.Player2_button1.grid(row=0, column=0, columnspan=2)

        self.Player2_button2 = tkinter.Button(self.Game_window,
                                              text="attack_2\n {}/{}".format(
                                                  self.Game.Player2.Attack2.Damage,
                                                  self.Game.Player2.Attack2.Hit_chance),
                                              justify="right", command=lambda: self.select_attack_for_player2(2))
        self.Player2_button2.grid(row=0, column=2, columnspan=2)

        self.Player2_button3 = tkinter.Button(self.Game_window,
                                              text="attack_3\n {}/{}".format(
                                                  self.Game.Player2.Attack3.Damage,
                                                  self.Game.Player2.Attack3.Hit_chance),
                                              justify="right", command=lambda: self.select_attack_for_player2(3))
        self.Player2_button3.grid(row=1, column=0, columnspan=2)

        self.Player2_button4 = tkinter.Button(self.Game_window,
                                              text="attack_4\n {}/{}".format(
                                                  self.Game.Player2.Attack4.Damage,
                                                  self.Game.Player2.Attack4.Hit_chance),
                                              justify="right", command=lambda: self.select_attack_for_player2(4))
        self.Player2_button4.grid(row=1, column=2, columnspan=2)


        # health bars
        self.Player1_health_bar = ttk.Progressbar(self.Game_window,
                                                  orient="horizontal", length=self.Window_width,
                                                  maximum=self.Game.Player1.HP, value=self.Game.Player1.HP)
        self.Player1_health_bar.grid(row=5, column=1, columnspan=2)
        self.Player1_shown_health = self.Game.Player1.HP # TODO numvar?

        self.Player2_health_bar = ttk.Progressbar(self.Game_window,
                                                  orient="horizontal", length=self.Window_width,
                                                  maximum=self.Game.Player2.HP, value=self.Game.Player2.HP)
        self.Player2_health_bar.grid(row=2, column=1, columnspan=2)
        self.Player2_shown_health = self.Game.Player2.HP # TODO numvar?


        # caption
        self.Feedback_caption = tkinter.StringVar(master, value="Welcome!")
        tkinter.Label(master, textvariable=self.Feedback_caption).pack()


        # game image
        self.Game_picture = tkinter.Canvas(self.Game_window, background='white')
        self.Game_picture.grid(row=3, rowspan=2, column=0, columnspan=4)

        # creating background
        self.Background_image=tkinter.PhotoImage(file='background.png')
        self.Background = self.Game_picture.create_image(200, 200, image=self.Background_image)

        # creating sprites
        self.Player1_sprite_image=tkinter.PhotoImage(file='{}.png'.format(self.Game.Player1.Name))
        self.Player1_sprite = self.Game_picture.create_image(GUI.Window_width,
                                                             GUI.Window_height * 3 // 4,
                                                             image=self.Player1_sprite_image)

        self.Player2_sprite_image=tkinter.PhotoImage(file='{}.png'.format(self.Game.Player2.Name))
        self.Player2_sprite = self.Game_picture.create_image(GUI.Window_width,
                                                             GUI.Window_height // 4,
                                                             image=self.Player2_sprite_image)


    ##### - GAME & GUI METHODS - #####

    def start_new_game(self, player1, player2):
        """ starts a new game """
        self.Game = Game.Game()
        self.Player1 = player1
        self.Player2 = player2
        # start with player 1
        self.Player1.play()


    def make_attack(self, selected_attack):
        """ makes an attack """
        # TODO make Game.take_turn return the active player
        # TODO remove winner from take_turn return
        (active_player, hit_check, damage_dealt) = self.Game.take_turn(selected_attack)
        # the game continues
        if self.Game.Game_active == True:
            self.show_turn_results(active_player, hit_check, damage_dealt)
        # if the game is over
        else:
            self.show_turn_results(active_player, hit_check, damage_dealt)
            self.end_game()


    def end_game(self):
        """ ends the game """
        self.Game_picture.create_text(200, 150, font=("Purisa", 20), text='GAME OVER')
        self.Feedback_caption.set("Game Over!")
        # TODO unbind the buttons / disable playing


    def show_turn_results(self, active_player, hit_check, damage_dealt): # # default value=zero?
        """ updates the current state of the game in the GUI """
        # first case if the attack landed
        if hit_check == True:
            if active_player == 'Player 1':
                self.Player2_shown_health = self.Game.Player2.HP
                self.Player2_health_bar["value"] = self.Player2_shown_health
                self.Feedback_caption.set("{0} suffers {1} damage. {0}'s turn".format(self.Game.Player2.Name,
                                                                                      damage_dealt))
            elif active_player == 'Player 2':
                self.Player1_shown_health = self.Game.Player1.HP
                self.Player1_health_bar["value"] = self.Player1_shown_health
                self.Feedback_caption.set("{0} suffers {1} damage. {0}'s turn".format(self.Game.Player1.Name,
                                                                                      damage_dealt))
            else:
                assert False, "invalid player"
        # the attack missed
        else:
            self.Feedback_caption.set("Missed! {}'s turn.".format(self.Game.Current_player.Name))

    ###  METHODS FOR ATTACK BUTTONS ###

    def select_attack_for_player1(self, attack_number):
        """ selects an attack for Player 1 after receiving the attack number """
        if self.Game.Current_player == self.Game.Player1:
            if attack_number == 1:
                self.Player1.make_attack(self.Game.Player1.Attack1)
            elif attack_number == 2:
                self.Player1.make_attack(self.Game.Player1.Attack2)
            elif attack_number == 3:
                self.Player1.make_attack(self.Game.Player1.Attack3)
            elif attack_number == 4:
                self.Player1.make_attack(self.Game.Player1.Attack4)
        else:
            print("Not your turn!")
            pass
            # TODO print warning?


    def select_attack_for_player2(self, attack_number):
        """ selects an attack for Player 2 after receiving the attack number """
        if self.Game.Current_player == self.Game.Player2:
            if attack_number == 1:
                self.Player2.make_attack(self.Game.Player2.Attack1)
            elif attack_number == 2:
                self.Player2.make_attack(self.Game.Player2.Attack2)
            elif attack_number == 3:
                self.Player2.make_attack(self.Game.Player2.Attack3)
            elif attack_number == 4:
                self.Player2.make_attack(self.Game.Player2.Attack4)
        else:
            print("Not your turn!")
            pass
            # TODO print warning

    ###  METHODS FOR GAME OPTIONS MENU ###

    def quit(self):
        """ closes the game window """
        root.destroy()

    def help(self):
        """Instructions for players"""
        Help = tkinter.Toplevel()
        Help.title("Help")

        General = tkinter.Frame(Help)
        General.pack(expand="yes", fill="both")
        Gen_instructions = tkinter.Label(General, text="Instructions for Duel Game")
        Gen_instructions.pack()

        Modifiers = tkinter.Frame(Help)
        Modifiers.pack(expand="yes", fill="both")
        Mod_instructions = tkinter.Label(Modifiers, text="Instructions for Modifiers")
        Mod_instructions.pack()

        Attacks = tkinter.Frame(Help)
        Attacks.pack(expand="yes", fill="both")
        Att_instructions = tkinter.Label(Modifiers, text="Instructions for Attacks")
        Att_instructions.pack()


app = GUI(root)


root.mainloop()