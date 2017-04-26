### THE USER INTERFACE
import tkinter
from tkinter import ttk
import Game

root = tkinter.Tk()
# TODO GET A NAME
root.title("Duel Game")

class GUI():

    #selecting window size by hand:
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
        self.Player1_Button1 = tkinter.Button(self.Game_window, text="attack_1\n {}/{}".format("50", "80"),justify="right", command=self.attack1)
        #format(Game.Game.Player_1.Attack1.Damage, Game.Game.Player_1.Attack1.Hit_chance)
        self.Player1_Button1.grid(row=6, column=0, columnspan=2, rowspan=1)

        self.Player1_Button2 = tkinter.Button(self.Game_window, text="attack_2\n {}/{}".format("50", "80"),justify="right", command=self.attack2)
        self.Player1_Button2.grid(row=6, column=2, columnspan=2)

        self.Player1_Button3 = tkinter.Button(self.Game_window, text="attack_3\n {}/{}".format("50", "80"),justify="right", command=self.attack3)
        self.Player1_Button3.grid(row=7, column=0, columnspan=2)

        self.Player1_Button4 = tkinter.Button(self.Game_window, text="attack_4\n {}/{}".format("50", "80"),justify="right", command=self.attack4)
        self.Player1_Button4.grid(row=7, column=2, columnspan=2)


        # creating the buttons for player 2
        # player 2 is at the top of the screen
        self.Player2_Button1 = tkinter.Button(self.Game_window, text="attack_1\n {}/{}".format("50", "80"),justify="right", command=self.attack5)
        self.Player2_Button1.grid(row=0, column=0, columnspan=2)

        self.Player2_Button2 = tkinter.Button(self.Game_window, text="attack_2\n {}/{}".format("50", "80"),justify="right", command=self.attack6)
        self.Player2_Button2.grid(row=0, column=2, columnspan=2)

        self.Player2_Button3 = tkinter.Button(self.Game_window, text="attack_3\n {}/{}".format("50", "80"),justify="right", command=self.attack7)
        self.Player2_Button3.grid(row=1, column=0, columnspan=2)

        self.Player2_Button4 = tkinter.Button(self.Game_window, text="attack_4\n {}/{}".format("50", "80"),justify="right", command=self.attack8)
        self.Player2_Button4.grid(row=1, column=2, columnspan=2)


        # creating the health bars
        self.Player1_Health_Bar = ttk.Progressbar(self.Game_window, orient="horizontal", length=200, maximum=1000,
                                                  value=1000)
        self.Player1_Health_Bar.grid(row=5, column=1, columnspan=2)
        self.Player1_Health = 1000

        self.Player1_Health_Bar = ttk.Progressbar(self.Game_window, orient="horizontal", length=200, maximum=1000,
                                                  value=1000)
        self.Player1_Health_Bar.grid(row=2, column=1, columnspan=2)
        self.Player1_Health = 1000

        # for checking if the healthbar works
        #self.Test_Button = tkinter.Button(self.Game_window, text="test_punch", command=self.deal_damage)
        #self.Test_Button.grid(row=5, column=3)


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
        self.Game_menu.add_command(label="New game", command=self.new_game)
        self.Game_menu.add_command(label="Help", command=self.help)


    # but why?
    def draw_game_picture(self):
        '''draws the image of the game'''
        self.Game_picture.create_line(0, 0, 20, 20)
        # TODO
        # player character images have to be added
        # possible different images on victory/loss/game modifiers

    # functions called by the buttons
    # they are gonna be in the game mechanincs file, this is placeholder
    def attack1(self):
        #TODO
        pass

    def attack2(self):
        #TODO
        pass

    def attack3(self):
        #TODO
        pass

    def attack4(self):
        #TODO
        pass

    def attack5(self):
        # TODO
        pass

    def attack6(self):
        # TODO
        pass

    def attack7(self):
        # TODO
        pass

    def attack8(self):
        # TODO
        pass

    def quit(self):
        # TODO
        pass

    def new_game(self):
        # TODO
        pass

    def help(self):
        #TODO
        pass

    def deal_damage(self):
        self.Player1_Health -= 50
        self.Player1_Health_Bar["value"] = self.Player1_Health




# TODO window name,...
app = GUI(root)

root.mainloop()
