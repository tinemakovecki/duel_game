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
        self.game = None
        self.player1 = None
        self.player2 = None

        # window
        self.game_window = tkinter.Frame(master, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

        # Main menu
        self.main_menu = tkinter.Menu(master)
        master.config(menu=self.main_menu)

        # Submenu
        self.game_options_menu = tkinter.Menu(self.main_menu)
        self.main_menu.add_cascade(label="Game", menu=self.game_options_menu)
        self.game_options_menu.add_command(label="Quit", command=self.quit)
        self.game_options_menu.add_command(label="New game",
                                           command=lambda: self.start_new_game(Player.Human(self),
                                                                               Player.Human(self)))
        # TODO add restart
        self.game_options_menu.add_command(label="Help", command=self.help)


        # buttons
        # player 1 is at the bottom
        self.player1_button1_text = tkinter.StringVar()
        self.player1_button1 = tkinter.Button(self.game_window, height=2, width=8,
                                              textvariable=self.player1_button1_text,
                                              justify="right",
                                              command=lambda: self.select_attack_for_player1(1))
        self.player1_button1.grid(row=10, column=0, columnspan=2, rowspan=1)

        self.player1_button2_text = tkinter.StringVar()
        self.player1_button2 = tkinter.Button(self.game_window, height=2, width=8,
                                              textvariable=self.player1_button2_text,
                                              justify="right",
                                              command=lambda: self.select_attack_for_player1(2))
        self.player1_button2.grid(row=10, column=2, columnspan=2)

        self.player1_button3_text = tkinter.StringVar()
        self.player1_button3 = tkinter.Button(self.game_window, height=2, width=8,
                                              textvariable=self.player1_button3_text,
                                              justify="right",
                                              command=lambda: self.select_attack_for_player1(3))
        self.player1_button3.grid(row=11, column=0, columnspan=2)

        self.player1_button4_text = tkinter.StringVar()
        self.player1_button4 = tkinter.Button(self.game_window, height=2, width=8,
                                              textvariable=self.player1_button4_text,
                                              justify="right",
                                              command=lambda: self.select_attack_for_player1(4))
        self.player1_button4.grid(row=11, column=2, columnspan=2)


        # player 2 is at the top
        self.player2_button1_text = tkinter.StringVar()
        self.player2_button1 = tkinter.Button(self.game_window, height=2, width=8,
                                              textvariable=self.player2_button1_text,
                                              justify="right",
                                              command=lambda: self.select_attack_for_player2(1))
        self.player2_button1.grid(row=0, column=0, columnspan=2)

        self.player2_button2_text = tkinter.StringVar()
        self.player2_button2 = tkinter.Button(self.game_window, height=2, width=8,
                                              textvariable=self.player2_button2_text,
                                              justify="right",
                                              command=lambda: self.select_attack_for_player2(2))
        self.player2_button2.grid(row=0, column=2, columnspan=2)

        self.player2_button3_text = tkinter.StringVar()
        self.player2_button3 = tkinter.Button(self.game_window, height=2, width=8,
                                              textvariable=self.player2_button3_text,
                                              justify="right",
                                              command=lambda: self.select_attack_for_player2(3))
        self.player2_button3.grid(row=1, column=0, columnspan=2)

        self.player2_button4_text = tkinter.StringVar()
        self.player2_button4 = tkinter.Button(self.game_window, height=2, width=8,
                                              textvariable=self.player2_button4_text,
                                              justify="right",
                                              command=lambda: self.select_attack_for_player2(4))
        self.player2_button4.grid(row=1, column=2, columnspan=2)


        # declaring health bars and modifiers feedback caption, they are changed later
        self.player1_health_bar = None
        self.player1_shown_health = None

        self.player2_health_bar = None
        self.player2_shown_health = None

        self.feedback_modifiers_player1_text = tkinter.StringVar(self.game_window)
        self.feedback_modifiers_player2_text = tkinter.StringVar(self.game_window)
        self.feedback_modifiers_player1 = None
        self.feedback_modifiers_player2 = None


        # caption
        self.feedback_caption_text = tkinter.StringVar(self.game_window, value="Welcome!")
        self.feedback_caption = tkinter.Label(master, textvariable=self.feedback_caption_text)
        self.feedback_caption.grid(row=12)


        # game image
        self.game_picture = tkinter.Canvas(self.game_window, background='white')
        self.game_picture.grid(row=5, rowspan=2, column=0, columnspan=4)

        # creating background
        self.background_image = tkinter.PhotoImage(file='background.png')
        self.background = self.game_picture.create_image(200, 200, image=self.background_image)

        # creating sprites
        self.player1_sprite_image = None
        self.player1_sprite = None

        self.player2_sprite_image = None
        self.player2_sprite = None


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
                                                       command=lambda:
                                                       self.start_new_game(Player.Human(self),
                                                                           Computer.Computer(self, Minimax.Minimax(3))))

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

    ##### - GRAPHICAL ELEMENTS TAGS - #####

    TAG_RESULT = 'result'

    ##### - GAME & GUI METHODS - #####

    def start_new_game(self, player1, player2):
        """ starts a new game """
        self.interrupt_players()

        self.game = Game.Game()
        self.player1 = player1
        self.player2 = player2

        # show the main game window
        self.new_game_display.grid_remove()
        self.new_game_button_human.grid_remove()
        self.new_game_button_computer.grid_remove()
        self.game_window.grid(row=0)
        self.feedback_caption.grid(row=12)

        # changing the text on player 1 buttons
        self.player1_button1_text.set("{}\n {}/{}".format(self.game.player1.attack1.name,
                                                          self.game.player1.attack1.damage,
                                                          self.game.player1.attack1.hit_chance))

        self.player1_button2_text.set("{}\n {}/{}".format(self.game.player1.attack2.name,
                                                          self.game.player1.attack2.damage,
                                                          self.game.player1.attack2.hit_chance))

        self.player1_button3_text.set("{}\n {}/{}".format(self.game.player1.attack3.name,
                                                          self.game.player1.attack3.damage,
                                                          self.game.player1.attack3.hit_chance))

        self.player1_button4_text.set("{}\n {}/{}".format(self.game.player1.attack4.name,
                                                          self.game.player1.attack4.damage,
                                                          self.game.player1.attack4.hit_chance))

        # changing the text on player 2 buttons
        self.player2_button1_text.set("{}\n {}/{}".format(self.game.player2.attack1.name,
                                                          self.game.player2.attack1.damage,
                                                          self.game.player2.attack1.hit_chance))

        self.player2_button2_text.set("{}\n {}/{}".format(self.game.player2.attack2.name,
                                                          self.game.player2.attack2.damage,
                                                          self.game.player2.attack2.hit_chance))

        self.player2_button3_text.set("{}\n {}/{}".format(self.game.player2.attack3.name,
                                                          self.game.player2.attack3.damage,
                                                          self.game.player2.attack3.hit_chance))

        self.player2_button4_text.set("{}\n {}/{}".format(self.game.player2.attack4.name,
                                                          self.game.player2.attack4.damage,
                                                          self.game.player2.attack4.hit_chance))

        # reseting the variable captions
        self.feedback_modifiers_player1_text.set("No modifiers affecting {}".format(self.game.player1.name))
        self.feedback_modifiers_player2_text.set("No modifiers affecting {}".format(self.game.player2.name))
        self.feedback_caption_text.set("Welcome!")


        self.feedback_modifiers_player1 = tkinter.Label(self.game_window, height=2, wraplength=WINDOW_WIDTH * 1.9,
                                                        textvariable=self.feedback_modifiers_player1_text)
        self.feedback_modifiers_player1.grid(row=7, rowspan=2, column=0, columnspan=4)

        self.feedback_modifiers_player2 = tkinter.Label(self.game_window, height=2, wraplength=WINDOW_WIDTH * 1.9,
                                                        textvariable=self.feedback_modifiers_player2_text)
        self.feedback_modifiers_player2.grid(row=2, rowspan=2, column=0, columnspan=4)


        # setting and showing healthbars
        self.player1_health_bar = ttk.Progressbar(self.game_window,
                                                  orient="horizontal",
                                                  length=WINDOW_WIDTH,
                                                  maximum=self.game.player1.hp,
                                                  value=self.game.player1.hp)
        self.player1_health_bar.grid(row=9, column=1, columnspan=2)
        self.player1_shown_health = self.game.player1.hp # TODO numvar?!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        self.player2_health_bar = ttk.Progressbar(self.game_window,
                                                  orient="horizontal",
                                                  length=WINDOW_WIDTH,
                                                  maximum=self.game.player2.hp,
                                                  value=self.game.player2.hp)
        self.player2_health_bar.grid(row=4, column=1, columnspan=2)
        self.player2_shown_health = self.game.player2.hp # TODO numvar?


        # loading player sprites
        self.player1_sprite_image = tkinter.PhotoImage(file='{}.png'.format(self.game.player1.name))
        self.player1_sprite = self.game_picture.create_image(WINDOW_WIDTH,
                                                             WINDOW_HEIGHT * 3 // 4,
                                                             image=self.player1_sprite_image)

        self.player2_sprite_image=tkinter.PhotoImage(file='{}.png'.format(self.game.player2.name))
        self.player2_sprite = self.game_picture.create_image(WINDOW_WIDTH,
                                                             WINDOW_HEIGHT // 4,
                                                             image=self.player2_sprite_image)

        # start with player 1
        self.player1.play()


    def make_attack(self, selected_attack, certain_hit=None):
        """ makes an attack """
        (active_player, hit_check, damage_dealt) = self.game.take_turn(selected_attack, certain_hit)
        # the game continues
        if self.game.game_active:
            # show what happened this turn
            self.show_turn_results(active_player, hit_check, damage_dealt)

            # start the next turn
            if self.game.current_player == self.game.player1:
                self.player1.play()
            elif self.game.current_player == self.game.player2:
                self.player2.play()

        # if the game is over
        else:
            self.show_turn_results(active_player, hit_check, damage_dealt)
            self.end_game()


    def end_game(self):
        """ ends the game """
        self.game_window.grid_remove()
        self.feedback_caption.grid_remove()
        self.feedback_modifiers_player1.grid_remove()
        self.feedback_modifiers_player2.grid_remove()
        self.game_over_display.grid()
        self.restart_button.grid()
        if self.game.winner == "Player 1":
            self.game_over_display.create_text(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2,
                                               font=("Purisa", 20), justify="center",
                                               fill='white', tag=GUI.TAG_RESULT,
                                               text='GAME OVER\nwinner:\n{}'.format(self.game.player1.name))
        elif self.game.winner == "Player 2":
            self.game_over_display.create_text(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2,
                                               font=("Purisa", 20), justify="center",
                                               fill='white', tag=GUI.TAG_RESULT,
                                               text='GAME OVER\nwinner:\n{}'.format(self.game.player2.name))
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

        # clear last game's results
        self.game_over_display.delete(GUI.TAG_RESULT)

        # show the new game screen
        self.new_game_display.grid(row=0)
        self.new_game_button_human.grid(row=1)
        self.new_game_button_computer.grid(row=2)


    def interrupt_players(self):
        """ interrupt both players """
        logging.debug ("prekinjam igralce")
        if self.player1: self.player1.interrupt()
        if self.player2: self.player2.interrupt()


    def show_turn_results(self, active_player, hit_check, damage_dealt):  # # default value=zero?
        """ updates the current state of the game in the GUI """
        # first case if the attack landed
        if hit_check:
            if active_player == 'Player 1':
                self.player2_shown_health = self.game.player2.hp
                self.player2_health_bar["value"] = self.player2_shown_health
                self.feedback_caption_text.set("{0} suffers {1} damage. {0}'s turn".format(self.game.player2.name,
                                                                                           damage_dealt))
            elif active_player == 'Player 2':
                self.player1_shown_health = self.game.player1.hp
                self.player1_health_bar["value"] = self.player1_shown_health
                self.feedback_caption_text.set("{0} suffers {1} damage. {0}'s turn".format(self.game.player1.name,
                                                                                           damage_dealt))
            else:
                assert False, "invalid player"
            # updating modifiers feedback
            if len(self.game.player1.active_modifiers) == 0:
                self.feedback_modifiers_player1_text.set("No modifiers affecting {}".format(self.game.player1.name))
            else:
                name, damage_effect, hit_effect, target = self.game.player1.active_modifiers[0][1]
                mod_str = "{}:{}/{}".format(name, damage_effect, hit_effect)
                for (turn_number, mod) in self.game.player1.active_modifiers[1:]:
                    mod_str += ", {}:{}/{}".format(mod[0], mod[1], mod[2])
                self.feedback_modifiers_player1_text.set(
                    "Modifiers affecting {}: {}".format(self.game.player1.name, mod_str))
            if len(self.game.player2.active_modifiers) == 0:
                self.feedback_modifiers_player2_text.set("No modifiers affecting {}".format(self.game.player2.name))
            else:
                name, damage_effect, hit_effect, target = self.game.player2.active_modifiers[0][1]
                mod_str = "{}:{}/{}".format(name, damage_effect, hit_effect)
                for (turn_number, mod) in self.game.player2.active_modifiers[1:]:
                    mod_str += ", {}:{}/{}".format(mod[0], mod[1], mod[2])
                self.feedback_modifiers_player2_text.set(
                    "Modifiers affecting {}: {}".format(self.game.player2.name, mod_str))
        # the attack missed
        else:
            self.feedback_caption_text.set("Missed! {}'s turn.".format(self.game.current_player.name))

    ###  METHODS FOR ATTACK BUTTONS ###

    def select_attack_for_player1(self, attack_number, certain_hit=None):
        """ selects an attack for Player 1 after receiving the attack number """
        if self.game.current_player == self.game.player1:
            if attack_number == 1:
                self.player1.make_attack(self.game.player1.attack1, certain_hit)
                return self.game.player1.attack1
            elif attack_number == 2:
                self.player1.make_attack(self.game.player1.attack2, certain_hit)
                return self.game.player1.attack2
            elif attack_number == 3:
                self.player1.make_attack(self.game.player1.attack3, certain_hit)
                return self.game.player1.attack3
            elif attack_number == 4:
                self.player1.make_attack(self.game.player1.attack4, certain_hit)
                return self.game.player1.attack4
        else:
            return


    def select_attack_for_player2(self, attack_number, certain_hit=None):
        """ selects an attack for Player 2 after receiving a number, returns the selected attack """
        if self.game.current_player == self.game.player2:
            if attack_number == 1:
                self.player2.make_attack(self.game.player2.attack1, certain_hit)
                return self.game.player2.attack1
            elif attack_number == 2:
                self.player2.make_attack(self.game.player2.attack2, certain_hit)
                return self.game.player2.attack2
            elif attack_number == 3:
                self.player2.make_attack(self.game.player2.attack3, certain_hit)
                return self.game.player2.attack3
            elif attack_number == 4:
                self.player2.make_attack(self.game.player2.attack4, certain_hit)
                return self.game.player2.attack4
        else:
            return

    ###  METHODS FOR GAME OPTIONS MENU ###

    def quit(self):
        """ closes the game window """
        self.interrupt_players()
        root.destroy()

    def help(self):
        """Instructions for players"""
        help = tkinter.Toplevel()
        help.title("Help")

        general = tkinter.Frame(help)
        general.pack(expand="yes", fill="both")
        gen_instructions = tkinter.Label(general, text="Instructions for Duel Game")
        gen_instructions.pack()

        modifiers = tkinter.Frame(help)
        modifiers.pack(expand="yes", fill="both")
        mod_instructions = tkinter.Label(modifiers, text="Instructions for Modifiers")
        mod_instructions.pack()

        attacks = tkinter.Frame(help)
        attacks.pack(expand="yes", fill="both")
        att_instructions = tkinter.Label(modifiers, text="Instructions for Attacks")
        att_instructions.pack()


app = GUI(root)


root.mainloop()