# The script of the game goes in this file.

# The game starts here.

label start:

    scene bg room

    # These display lines of dialogue.

    "Welcome to Ren'Py Snakes and Ladders!"

    menu:
        "Do you need Tutorial?"
        "Yes":
            jump tutorial
        "No":
            jump setting

label tutorial:
    show tutorial1 at top
    "The main goal of Snakes and Ladders is to reach the end of the board, the tile 100, first"
    hide tutorial1
    show tutorial2 at truecenter
    "To roll the dice, click the Roll button or press Space"
    hide tutorial2
    show tutorial3 at truecenter
    "The Ladder is represented by a green space, while Snake is Red"
    "Darker tiles is the start of the ladder or snake, and lighter tiles is the end"
    "The symbol on the tiles tell the pair of snake or ladder"
    "If a piece stop on the start of a snake or a ladder, it will have to move to the end of said snake or ladder"
    hide tutorial3
    show tutorial4 at truecenter
    "If a player will go over the end of the board, they need to move back based on the remainder of the move"
    hide tutorial4
    "That's about it on how to play Snakes and Ladders."
    "Before that, lets set the game's setting!"

label setting:
    menu:
        "How many Player will play this round?"
        "2":
            $maxPlayer = 2
            $p3 = 0
            $p4 = 0

            menu:
                "What is Player 1?"
                "Human":
                    $p1 = 1
                "Computer":
                    $p1 = 2
            menu:
                "What is Player 2?"
                "Human":
                    $p2 = 1
                "Computer":
                    $p2 = 2
        "3":
            $maxPlayer = 3
            $p4 = 0
            menu:
                "What is Player 1?"
                "Human":
                    $p1 = 1
                "Computer":
                    $p1 = 2
            menu:
                "What is Player 2?"
                "Human":
                    $p2 = 1
                "Computer":
                    $p2 = 2
            menu:
                "What is Player 3?"
                "Human":
                    $p3 = 1
                "Computer":
                    $p3 = 2
        "4":
            $maxPlayer = 4
            menu:
                "What is Player 1?"
                "Human":
                    $p1 = 1
                "Computer":
                    $p1 = 2
            menu:
                "What is Player 2?"
                "Human":
                    $p2 = 1
                "Computer":
                    $p2 = 2
            menu:
                "What is Player 3?"
                "Human":
                    $p3 = 1
                "Computer":
                    $p3 = 2
            menu:
                "What is Player 4?"
                "Human":
                    $p4 = 1
                "Computer":
                    $p4 = 2

label start_game:
    window hide
    $ quick_menu = False

    # avoid rolling back and losing game state
    $ renpy.block_rollback()

    # disable Esc key menu to prevent the player from saving the game
    $ _game_menu_screen = None

    call screen sl(maxPlayer, p1, p2, p3, p4)

    # re-enable the Esc key menu
    $ _game_menu_screen = 'save'

    # avoid rolling back and entering the game again
    $ renpy.block_rollback()

    # restore rollback from this point on
    $ renpy.checkpoint()

    $ quick_menu = True
    window show

    "Thank you for playing!"

    return
