def input_number(prompt='Please enter a number: ', minimum=0, maximum=None):
    """Read a positive number with the given prompt."""

    while True:
        try:
            number = int(input(prompt))
            if (number < minimum or
                (maximum is not None and number > maximum)):
                    print('Number is not within range: {} to {}'.format(minimum, maximum))
            else:
                break

        except ValueError:
            print('You need to enter a number')
            continue

    return number


class Player(object):
    """Base class for different player types."""

    def __init__(self, name=None):
        self.name = name
        self.score = 0


    def add_score(self, player_score):

        self.score += player_score


    def __str__(self):
        """Returns player name and current score."""

        return str(self.name) + ": " + str(self.score)

class ComputerPlayer(Player):


    def __init__(self, number):
        name='Computer'
        
        super(ComputerPlayer, self).__init__(name)


    def keep_rolling(self, temp):

        while temp.value < 20:
            print("  CPU will roll ")
            return True
        print("  CPU will hold.")
        return False


class HumanPlayer(Player):
    def __init__(self, name):
        super(HumanPlayer, self).__init__(name)


    def keep_rolling(self, temp):
        """Asks the human player, if they want to keep rolling."""
        human_decision = input_number("  1 - Roll again, 0 - Hold? ", 0, 1)
        if human_decision == 1:
            return True
        else:
            return False
        
