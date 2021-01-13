class Menu:
    """
    Class that create the Menu section

    Methods
    -------
    display_home_screen(self)
        Display the home screen 
        
    __select_an_option(self, number_of_options)
        Ask the user to chose between 2 optionsm Get a substitute or Show favorites

    """
    def __init__(self):
        pass

    def display_home_screen(self):
        """
        Display the home screen 

        """
        options = ['Get a substitute', 'Show favorites']
        number_of_options = len(options)
        print('')
        print('Welcome to Pur Beurre,')
        print('')
    
        for option_position, option in enumerate(options):
            print('{}: {}'.format(option_position + 1, option))
            print('')
        self.__select_an_option(number_of_options)  

    def __select_an_option(self, number_of_options):
        """
        Ask the user to chose between 2 optionsm Get a substitute or Show favorites
        
        Parameters
        -------     
        number_of_options: int
        """     
        self.selected_option = int(input('Which action do you want to make? '))
        while self.selected_option not in [1, 2]:
            print('')
            self.selected_option = int(input("The action you chose doesn't exist. Please chose a valid action: "))

            