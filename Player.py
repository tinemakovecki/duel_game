### HUMAN PLAYER FILE

class Human():
    def __init__(self, gui):
        self.Gui = gui

    def play(self):
        ''' idles and waits '''
        pass

    def make_attack(self, selected, certain_hit):
        ''' makes an attack '''
        self.Gui.make_attack(selected, certain_hit)