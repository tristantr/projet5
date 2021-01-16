class Menu:
    """
    Class that create the Menu section

    Methods
    -------
    display_home_screen(self)
        Display the home screen

    __select_an_option(self)
        Ask the user to chose between 2 optionsm Get a substitute or Show favorites

    """

    def __init__(self):
        pass

    def display_home_screen(self):
        """
        Display the home screen

        """
        options = ["Get a substitute", "Show favorites"]
        print("")
        print("Welcome to Pur Beurre,")
        print("")

        for option_position, option in enumerate(options):
            print("{}: {}".format(option_position + 1, option))
            print("")
        self.__select_an_option()

    def __select_an_option(self):
        """
        Ask the user to chose between 2 options: Get a substitute or Show favorites
        """
        while True:
            try:
                self.selected_option = int(input("Which action do you want to make?  "))
                assert 0 < self.selected_option < 3
            except ValueError:
                print("")
                print("The action you chose doesn't exist.")
            except AssertionError:
                print("")
                print("The action you chose doesn't exist. Please enter a valid option")
            else:
                break
