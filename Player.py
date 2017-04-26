### HUMAN PLAYER FILE

class Human():
    def __init__(self, gui):
        self.Gui = gui

    def idle(self):
        ''' idles and waits '''
        pass

    def make_attack(self, selected):
        ''' makes an attack '''
        self.Gui.make_attack(selected)