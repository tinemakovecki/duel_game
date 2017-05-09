####### - COMUPTER PLAYER - #######

import threading


class Computer:
    def __init__(self, gui, algorithm):
        self.gui = gui
        self.algorithm = algorithm
        self.thinker = None


    def play(self):
        """ plays the turn selected by the algorithm """
        # creating a new thread for the algorithm which uses a copy of the game
        self.thinker = threading.Thread(
            target=lambda: self.algorithm.select_attack(self.gui.Game.copy()))

        # actually start the thread
        self.thinker.start()

        # checking if a turn has been selected
        self.gui.Game_window.after(100, self.check_move)


    def check_for_attack(self):
        """ checks if the algorithm has selected an attack each 100 ms """
        if self.algorithm.move is not None:
            # the attack selected by the algorithm is performed
            self.gui.make_attack(self.algorithm.chosen_attack)
            # the thinker thread has finished work, we remove it
            self.thinker = None
        else:
            # the algorithm hasn't found a move yet, check back later
            self.gui.Game_window.after(100, self.check_move())


    def interrupt(self):
        """ called by the GUI thread to interrupt the thinking algorithm """
        if self.thinker is not None:
            logging.debug("Canceling {0}".format(self.thinker))
            # telling the thinker thread to stop
            self.algorithm.interrupt()
            # wait for the thread to stop
            self.thinker.join()
            self.thinker = None
            # TODO add interrupt to GUI functions


    def make_attack(self, selected_attack, certain_hit):
        """ the computer ignores attack selected with a button in the GUI """
        pass