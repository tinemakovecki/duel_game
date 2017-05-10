####### - MAIN GAME FILE & USER INTERFACE - #######

import tkinter

def help():
    """ Instructions for players """
    help_app = tkinter.Toplevel()
    help_app.title("Help")

    tutorial_window = tkinter.Frame(help_app)
    tutorial_window.pack(expand="yes", fill="both")

    ### - TITLE - ###
    tutorial_title = tkinter.Label(tutorial_window,
                                   text="TUTORIAL",
                                   justify="left",
                                   font=("Purisa", 14))

    ### - FIRST PARAGRAPH - ###
    # introduction
    tutorial__paragraph_1_text = """
    This game is based on the battles in pokemon games.
    There are two players and each of them controls a
    creature. The monsters have a certain amount of
    health and a set of attacks they can do. When it's
    your turn, you select an attack to perform. If the
    attack hits it deals damage. You win when the other
    player has no more health left.
    """
    tutorial__paragraph_1 = tkinter.Label(tutorial_window,
                                          text=tutorial__paragraph_1_text,
                                          justify="left")

    ### - SECOND PARAGRAPH - ###
    # title
    tutorial__paragraph_2_title = tkinter.Label(tutorial_window,
                                                text="Attacks:",
                                                justify="left",
                                                font=("Purisa", 12))

    # paragraph
    tutorial__paragraph_2_text = """
    Each creature has 4 attacks and every button
    represents an attack. The text written on the
    button is the name, the damage it deals and the
    percentage chance for the attack to hit.
    """
    tutorial__paragraph_2 = tkinter.Label(tutorial_window,
                                          text=tutorial__paragraph_2_text,
                                          justify="left")

    ### - THIRD PARAGRAPH - ###
    # title
    tutorial__paragraph_3_title = tkinter.Label(tutorial_window,
                                                text="Modifiers:",
                                                justify="left",
                                                font=("Purisa", 12))

    # paragraph
    tutorial__paragraph_3_text = """
    When an attack hits it also has an extra effect
    besides dealing damage. It affects one of the
    creatures with a "modifier" that changes its
    damage and hit chance for a short amount of time.
    These effects last for three turns. If an attack
    is repeated its effect doesn't stack, instead it
    only refreshes.
    """
    tutorial__paragraph_3 = tkinter.Label(tutorial_window,
                                          text=tutorial__paragraph_3_text,
                                          justify="left")

    # pack the text elements in the right order
    tutorial_title.pack()
    tutorial__paragraph_1.pack()
    tutorial__paragraph_2_title.pack()
    tutorial__paragraph_2.pack()
    tutorial__paragraph_3_title.pack()
    tutorial__paragraph_3.pack()
