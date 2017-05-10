### HUMAN PLAYER FILE

class Human():
    def __init__(self, gui):
        self.gui = gui

    def play(self):
        ''' does nothing, waits for the player to select an attack '''
        pass

    def make_attack(self, selected, certain_hit):
        ''' makes an attack '''
        self.gui.make_attack(selected, certain_hit)

    def interrupt(self):
        """ happens when interrupting players, does nothing """
        pass