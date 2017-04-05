### THE USER INTERFACE
import tkinter

root = tkinter.Tk()
# TODO GET A NAME
root.title("Beyblade")

class GUI():

    #selecting window size by hand:
    Window_height = 300
    Window_width = 200

    def __init__(self, master):
        # creating the game window
        self.Game_window = tkinter.Frame(master, width=GUI.Window_width, height=GUI.Window_height)
        self.Game_window.pack()


        # TODO bigger buttons
        # creating the buttons for player 1
        # player 1 is at the bottom of the screen
        self.Player1_Button1 = tkinter.Button(self.Game_window, text="attack_1", command=self.attack1)
        self.Player1_Button1.grid(row=5, column=0)

        self.Player1_Button2 = tkinter.Button(self.Game_window, text="attack_2", command=self.attack2)
        self.Player1_Button2.grid(row=5, column=1)

        self.Player1_Button3 = tkinter.Button(self.Game_window, text="attack_3", command=self.attack3)
        self.Player1_Button3.grid(row=6, column=0)

        self.Player1_Button4 = tkinter.Button(self.Game_window, text="attack_4", command=self.attack4)
        self.Player1_Button4.grid(row=6, column=1)


        # creating the buttons for player 2
        # player 2 is at the top of the screen
        self.Player2_Button1 = tkinter.Button(self.Game_window, text="attack_1", command=self.attack5)
        self.Player2_Button1.grid(row=1, column=0)

        self.Player2_Button2 = tkinter.Button(self.Game_window, text="attack_2", command=self.attack6)
        self.Player2_Button2.grid(row=1, column=1)

        self.Player2_Button3 = tkinter.Button(self.Game_window, text="attack_3", command=self.attack7)
        self.Player2_Button3.grid(row=2, column=0)

        self.Player2_Button4 = tkinter.Button(self.Game_window, text="attack_4", command=self.attack8)
        self.Player2_Button4.grid(row=2, column=1)


        # HEALTH BARS AS A WIDGET? - TODO
        # creating the game image
        self.Game_picture = tkinter.Canvas(self.Game_window, background='white')
        self.Game_picture.grid(row=3, rowspan=2, column=0, columnspan=2)
        self.draw_game_picture()




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


# TODO window name,...
app = GUI(root)

root.mainloop()