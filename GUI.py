####### - MAIN GAME FILE & USER INTERFACE - #######

import logging
import tkinter
from tkinter import ttk
import Game
import Player
import Computer
import Minimax

root = tkinter.Tk()
root.title("Duel Game")

# TODO select/stretchable
WINDOW_HEIGHT = 300
WINDOW_WIDTH = 200

class GUI():


    def __init__(self, master):
        # not yet defined, just declared for __init__
        self.Game = None
        self.Player1 = None
        self.Player2 = None

        # window
        self.Game_window = tkinter.Frame(master, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

        # Main menu
        self.Main_menu = tkinter.Menu(master)
        master.config(menu=self.Main_menu)

        # Submenu
        self.Game_options_menu = tkinter.Menu(self.Main_menu)
        self.Main_menu.add_cascade(label="Game", menu=self.Game_options_menu)
        self.Game_options_menu.add_command(label="Quit", command=self.quit)
        self.Game_options_menu.add_command(label="New game",
                                           command=lambda: self.start_new_game(Player.Human(self),
                                                                               Player.Human(self)))
        # TODO add restart
        self.Game_options_menu.add_command(label="Help", command=self.help)


        # buttons
        # player 1 is at the bottom
        self.player1_button1_text = tkinter.StringVar()
        self.Player1_button1 = tkinter.Button(self.Game_window, height=2, width=8,
                                              textvariable=self.player1_button1_text,
                                              justify="right",
                                              command=lambda: self.select_attack_for_player1(1))
        self.Player1_button1.grid(row=10, column=0, columnspan=2, rowspan=1)

        self.player1_button2_text = tkinter.StringVar()
        self.Player1_button2 = tkinter.Button(self.Game_window, height=2, width=8,
                                              textvariable=self.player1_button2_text,
                                              justify="right",
                                              command=lambda: self.select_attack_for_player1(2))
        self.Player1_button2.grid(row=10, column=2, columnspan=2)

        self.player1_button3_text = tkinter.StringVar()
        self.Player1_button3 = tkinter.Button(self.Game_window, height=2, width=8,
                                              textvariable=self.player1_button3_text,
                                              justify="right",
                                              command=lambda: self.select_attack_for_player1(3))
        self.Player1_button3.grid(row=11, column=0, columnspan=2)

        self.player1_button4_text = tkinter.StringVar()
        self.Player1_button4 = tkinter.Button(self.Game_window, height=2, width=8,
                                              textvariable=self.player1_button4_text,
                                              justify="right",
                                              command=lambda: self.select_attack_for_player1(4))
        self.Player1_button4.grid(row=11, column=2, columnspan=2)


        # player 2 is at the top
        self.player2_button1_text = tkinter.StringVar()
        self.Player2_button1 = tkinter.Button(self.Game_window, height=2, width=8,
                                              textvariable=self.player2_button1_text,
                                              justify="right",
                                              command=lambda: self.select_attack_for_player2(1))
        self.Player2_button1.grid(row=0, column=0, columnspan=2)

        self.player2_button2_text = tkinter.StringVar()
        self.Player2_button2 = tkinter.Button(self.Game_window, height=2, width=8,
                                              textvariable=self.player2_button2_text,
                                              justify="right",
                                              command=lambda: self.select_attack_for_player2(2))
        self.Player2_button2.grid(row=0, column=2, columnspan=2)

        self.player2_button3_text = tkinter.StringVar()
        self.Player2_button3 = tkinter.Button(self.Game_window, height=2, width=8,
                                              textvariable=self.player2_button3_text,
                                              justify="right",
                                              command=lambda: self.select_attack_for_player2(3))
        self.Player2_button3.grid(row=1, column=0, columnspan=2)

        self.player2_button4_text = tkinter.StringVar()
        self.Player2_button4 = tkinter.Button(self.Game_window, height=2, width=8,
                                              textvariable=self.player2_button4_text,
                                              justify="right",
                                              command=lambda: self.select_attack_for_player2(4))
        self.Player2_button4.grid(row=1, column=2, columnspan=2)


        # declaring health bars and modifiers feedback caption, they are changed later
        self.Player1_health_bar = None
        self.Player1_shown_health = None

        self.Player2_health_bar = None
        self.Player2_shown_health = None

        self.feedback_modifiers_player1_text = tkinter.StringVar(self.Game_window)
        self.feedback_modifiers_player2_text = tkinter.StringVar(self.Game_window)
        self.feedback_modifiers_player1 = None
        self.feedback_modifiers_player2 = None


        # caption
        self.feedback_caption_text = tkinter.StringVar(self.Game_window, value="Welcome!")
        self.feedback_caption = tkinter.Label(master, textvariable=self.feedback_caption_text)
        self.feedback_caption.grid(row=12)


        # game image
        self.Game_picture = tkinter.Canvas(self.Game_window, background='white')
        self.Game_picture.grid(row=5, rowspan=2, column=0, columnspan=4)

        # creating background
        self.Background_image = tkinter.PhotoImage(file='background.png')
        self.Background = self.Game_picture.create_image(200, 200, image=self.Background_image)

        # creating sprites
        self.Player1_sprite_image = None
        self.Player1_sprite = None

        self.Player2_sprite_image = None
        self.Player2_sprite = None


        # game over screen
        self.restart_button = tkinter.Button(master,
                                             text='Restart',
                                             command=lambda: self.restart_game())
        self.game_over_display = tkinter.Canvas(master,
                                                width=WINDOW_WIDTH,
                                                height=WINDOW_HEIGHT,
                                                background='black')


        # new game screen
        self.new_game_button_human = tkinter.Button(master,
                                                       text='Start human game',
                                                       command=lambda: self.start_new_game(Player.Human(self),
                                                                                           Player.Human(self)))

        self.new_game_button_computer = tkinter.Button(master,
                                                       text='Start computer game',
                                                       command=lambda: self.start_new_game(Player.Human(self),
                                                                                           Computer.Computer(self,
                                                                                                             Minimax.Minimax(3))))

        self.new_game_display = tkinter.Canvas(master,
                                               width=WINDOW_WIDTH,
                                               height=WINDOW_HEIGHT,
                                               background='black')

        self.new_game_display.create_text(WINDOW_WIDTH / 2,
                                          WINDOW_HEIGHT / 2,
                                          font=("Purisa", 20),
                                          fill='white',
                                          text='WELCOME')

        self.new_game_display.grid(row=0)
        self.new_game_button_human.grid(row=1)
        self.new_game_button_computer.grid(row=2)

    ##### - GAME & GUI METHODS - #####

    def start_new_game(self, player1, player2):
        """ starts a new game """
        self.interrupt_players()

        self.Game = Game.Game()
        self.Player1 = player1
        self.Player2 = player2

        # show the main game window
        self.new_game_display.grid_remove()
        self.new_game_button_human.grid_remove()
        self.new_game_button_computer.grid_remove()
        self.Game_window.grid(row=0)
        self.feedback_caption.grid(row=12)

        # changing the text on player 1 buttons
        self.player1_button1_text.set("{}\n {}/{}".format(self.Game.Player1.Attack1.Name,
                                                          self.Game.Player1.Attack1.Damage,
                                                          self.Game.Player1.Attack1.Hit_chance))

        self.player1_button2_text.set("{}\n {}/{}".format(self.Game.Player1.Attack2.Name,
                                                          self.Game.Player1.Attack2.Damage,
                                                          self.Game.Player1.Attack2.Hit_chance))

        self.player1_button3_text.set("{}\n {}/{}".format(self.Game.Player1.Attack3.Name,
                                                          self.Game.Player1.Attack3.Damage,
                                                          self.Game.Player1.Attack3.Hit_chance))

        self.player1_button4_text.set("{}\n {}/{}".format(self.Game.Player1.Attack4.Name,
                                                          self.Game.Player1.Attack4.Damage,
                                                          self.Game.Player1.Attack4.Hit_chance))

        # changing the text on player 2 buttons
        self.player2_button1_text.set("{}\n {}/{}".format(self.Game.Player2.Attack1.Name,
                                                          self.Game.Player2.Attack1.Damage,
                                                          self.Game.Player2.Attack1.Hit_chance))

        self.player2_button2_text.set("{}\n {}/{}".format(self.Game.Player2.Attack2.Name,
                                                          self.Game.Player2.Attack2.Damage,
                                                          self.Game.Player2.Attack2.Hit_chance))

        self.player2_button3_text.set("{}\n {}/{}".format(self.Game.Player2.Attack3.Name,
                                                          self.Game.Player2.Attack3.Damage,
                                                          self.Game.Player2.Attack3.Hit_chance))

        self.player2_button4_text.set("{}\n {}/{}".format(self.Game.Player2.Attack4.Name,
                                                          self.Game.Player2.Attack4.Damage,
                                                          self.Game.Player2.Attack4.Hit_chance))

        # reseting the variable captions
        self.feedback_modifiers_player1_text.set("No modifiers affecting {}".format(self.Game.Player1.Name))
        self.feedback_modifiers_player2_text.set("No modifiers affecting {}".format(self.Game.Player2.Name))
        self.feedback_caption_text.set("Welcome!")


        self.feedback_modifiers_player1 = tkinter.Label(self.Game_window, height=2, wraplength=WINDOW_WIDTH * 1.9,
                                                        textvariable=self.feedback_modifiers_player1_text)
        self.feedback_modifiers_player1.grid(row=7, rowspan=2, column=0, columnspan=4)

        self.feedback_modifiers_player2 = tkinter.Label(self.Game_window, height=2, wraplength=WINDOW_WIDTH * 1.9,
                                                        textvariable=self.feedback_modifiers_player2_text)
        self.feedback_modifiers_player2.grid(row=2, rowspan=2, column=0, columnspan=4)


        # setting and showing healthbars
        self.Player1_health_bar = ttk.Progressbar(self.Game_window,
                                                  orient="horizontal",
                                                  length=WINDOW_WIDTH,
                                                  maximum=self.Game.Player1.HP,
                                                  value=self.Game.Player1.HP)
        self.Player1_health_bar.grid(row=9, column=1, columnspan=2)
        self.Player1_shown_health = self.Game.Player1.HP # TODO numvar?!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        self.Player2_health_bar = ttk.Progressbar(self.Game_window,
                                                  orient="horizontal",
                                                  length=WINDOW_WIDTH,
                                                  maximum=self.Game.Player2.HP,
                                                  value=self.Game.Player2.HP)
        self.Player2_health_bar.grid(row=4, column=1, columnspan=2)
        self.Player2_shown_health = self.Game.Player2.HP # TODO numvar?


        # loading player sprites
        self.Player1_sprite_image = tkinter.PhotoImage(file='{}.png'.format(self.Game.Player1.Name))
        self.Player1_sprite = self.Game_picture.create_image(WINDOW_WIDTH,
                                                             WINDOW_HEIGHT * 3 // 4,
                                                             image=self.Player1_sprite_image)

        self.Player2_sprite_image=tkinter.PhotoImage(file='{}.png'.format(self.Game.Player2.Name))
        self.Player2_sprite = self.Game_picture.create_image(WINDOW_WIDTH,
                                                             WINDOW_HEIGHT // 4,
                                                             image=self.Player2_sprite_image)

        # start with player 1
        self.Player1.play()


    def make_attack(self, selected_attack, certain_hit=None):
        """ makes an attack """
        (active_player, hit_check, damage_dealt) = self.Game.take_turn(selected_attack, certain_hit)
        # the game continues
        if self.Game.Game_active:
            # show what happened this turn
            self.show_turn_results(active_player, hit_check, damage_dealt)

            # start the next turn
            if self.Game.Current_player == self.Game.Player1:
                self.Player1.play()
            elif self.Game.Current_player == self.Game.Player2:
                self.Player2.play()

        # if the game is over
        else:
            self.show_turn_results(active_player, hit_check, damage_dealt)
            self.end_game()


    def end_game(self):
        """ ends the game """
        self.Game_window.grid_remove()
        self.feedback_caption.grid_remove()
        self.feedback_modifiers_player1.grid_remove()
        self.feedback_modifiers_player2.grid_remove()
        self.game_over_display.grid()
        self.restart_button.grid()
        if self.Game.Winner == "Player 1":
            self.game_over_display.create_text(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2,
                                               font=("Purisa", 20), justify="center", fill='white',
                                               text='GAME OVER\nwinner:\n{}'.format(self.Game.Player1.Name))
        elif self.Game.Winner == "Player 2":
            self.game_over_display.create_text(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2,
                                               font=("Purisa", 20), justify="center", fill='white',
                                               text='GAME OVER\nwinner:\n{}'.format(self.Game.Player2.Name))
        else:
            assert False; "Game is not over yet"

        # TODO unbind the buttons / disable playing
        # self.Player = None


    def restart_game(self):
        """ switches the game back to the starting window """
        # hide the game over screen
        self.game_over_display.grid_remove()
        self.restart_button.grid_remove()
        self.feedback_modifiers_player1.grid_remove()
        self.feedback_modifiers_player2.grid_remove()

        # show the new game screen
        self.new_game_display.grid(row=0)
        self.new_game_button_human.grid(row=1)
        self.new_game_button_computer.grid(row=1)


    def interrupt_players(self):
        """ interrupt both players """
        logging.debug ("prekinjam igralce")
        if self.Player1: self.Player1.interrupt()
        if self.Player2: self.Player2.interrupt()


    def show_turn_results(self, active_player, hit_check, damage_dealt):  # # default value=zero?
        """ updates the current state of the game in the GUI """
        # first case if the attack landed
        if hit_check:
            if active_player == 'Player 1':
                self.Player2_shown_health = self.Game.Player2.HP
                self.Player2_health_bar["value"] = self.Player2_shown_health
                self.feedback_caption_text.set("{0} suffers {1} damage. {0}'s turn".format(self.Game.Player2.Name,
                                                                                           damage_dealt))
            elif active_player == 'Player 2':
                self.Player1_shown_health = self.Game.Player1.HP
                self.Player1_health_bar["value"] = self.Player1_shown_health
                self.feedback_caption_text.set("{0} suffers {1} damage. {0}'s turn".format(self.Game.Player1.Name,
                                                                                           damage_dealt))
            else:
                assert False, "invalid player"
            # updating modifiers feedback
            if len(self.Game.Player1.Active_modifiers) == 0:
                self.feedback_modifiers_player1_text.set("No modifiers affecting {}".format(self.Game.Player1.Name))
            else:
                name, damage_effect, hit_effect, target = self.Game.Player1.Active_modifiers[0][1]
                mod_str = "{}:{}/{}".format(name, damage_effect, hit_effect)
                for (turn_number, mod) in self.Game.Player1.Active_modifiers[1:]:
                    mod_str += ", {}:{}/{}".format(mod[0], mod[1], mod[2])
                self.feedback_modifiers_player1_text.set(
                    "Modifiers affecting {}: {}".format(self.Game.Player1.Name, mod_str))
            if len(self.Game.Player2.Active_modifiers) == 0:
                self.feedback_modifiers_player2_text.set("No modifiers affecting {}".format(self.Game.Player2.Name))
            else:
                name, damage_effect, hit_effect, target = self.Game.Player2.Active_modifiers[0][1]
                mod_str = "{}:{}/{}".format(name, damage_effect, hit_effect)
                for (turn_number, mod) in self.Game.Player2.Active_modifiers[1:]:
                    mod_str += ", {}:{}/{}".format(mod[0], mod[1], mod[2])
                self.feedback_modifiers_player2_text.set(
                    "Modifiers affecting {}: {}".format(self.Game.Player2.Name, mod_str))
        # the attack missed
        else:
            self.feedback_caption_text.set("Missed! {}'s turn.".format(self.Game.Current_player.Name))

    ###  METHODS FOR ATTACK BUTTONS ###

    def select_attack_for_player1(self, attack_number, certain_hit=None):
        """ selects an attack for Player 1 after receiving the attack number """
        if self.Game.Current_player == self.Game.Player1:
            if attack_number == 1:
                self.Player1.make_attack(self.Game.Player1.Attack1, certain_hit)
                return self.Game.Player1.Attack1
            elif attack_number == 2:
                self.Player1.make_attack(self.Game.Player1.Attack2, certain_hit)
                return self.Game.Player1.Attack2
            elif attack_number == 3:
                self.Player1.make_attack(self.Game.Player1.Attack3, certain_hit)
                return self.Game.Player1.Attack3
            elif attack_number == 4:
                self.Player1.make_attack(self.Game.Player1.Attack4, certain_hit)
                return self.Game.Player1.Attack4
        else:
            return


    def select_attack_for_player2(self, attack_number, certain_hit=None):
        """ selects an attack for Player 2 after receiving a number, returns the selected attack """
        if self.Game.Current_player == self.Game.Player2:
            if attack_number == 1:
                self.Player2.make_attack(self.Game.Player2.Attack1, certain_hit)
                return self.Game.Player2.Attack1
            elif attack_number == 2:
                self.Player2.make_attack(self.Game.Player2.Attack2, certain_hit)
                return self.Game.Player2.Attack2
            elif attack_number == 3:
                self.Player2.make_attack(self.Game.Player2.Attack3, certain_hit)
                return self.Game.Player2.Attack3
            elif attack_number == 4:
                self.Player2.make_attack(self.Game.Player2.Attack4, certain_hit)
                return self.Game.Player2.Attack4
        else:
            return

    ###  METHODS FOR GAME OPTIONS MENU ###

    def quit(self):
        """ closes the game window """
        self.interrupt_players()
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