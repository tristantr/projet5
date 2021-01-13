import sys

class Global_section():

    """
    Superclass to define the user path

    Methods
    -------
    __launch_program(self, menu_interface)
        Launch our program, depending on the choice of the user

    __launch_substitution_program(self)
        Look for a substitute

    __select_an_option(self)
        Display options available after getting a substitute

    __add_to_favorite(self, substitute_id)
        Add a product to the Favorite table

    __go_back_to_menu(self)
        Go back to the menu section
    """

    def __init__(self, menu_interface, user_interface, methods_for_db, substitute):
        """
        Parameters
        -------
        menu_interface: instance of Menu class

        user_interface: instance of User_interface class

        methods_for_db: instance of Methods class in database package

        substitute: instance of Substitution class

        """
        self.menu_interface = menu_interface 
        self.user_interface = user_interface
        self.methods_for_db = methods_for_db
        self.substitute = substitute
        self.__launch_program()

    def __launch_program(self):
        """
        Launch our program, depending on the choice of the user

        """
        self.menu_interface.display_home_screen()
        if self.menu_interface.selected_option == 1:
            self.__launch_substitution_program()
            self.__select_an_option()            
        else:
            self.user_interface.display_favorites()
            self.__go_back_to_menu()

    def __launch_substitution_program(self):
        """
        Look for a substitute
        """
        self.user_interface.display_user_interface()
        self.substitute.launch_substitution_program(self.user_interface.id_of_the_product_to_substitute, self.user_interface.selected_category_id)

        if self.substitute.products_with_better_nutriscores == []:
            self.user_interface.print_best_nutriscore_messages()
            self.user_interface.substitute_id = self.user_interface.id_of_the_product_to_substitute
        else:
            self.user_interface.show_a_substitute(self.substitute.substitute_id)
                    
    def __select_an_option(self):
        """
        Display options available after getting a substitute
        """        
        self.user_interface.select_an_option()

        if self.user_interface.selected_option == 1:
            self.__add_to_favorite(self.substitute.substitute_id)
            self.__go_back_to_menu()

        elif self.user_interface.selected_option == 2:
            if self.substitute.products_with_better_nutriscores == []:
                self.user_interface.print_best_nutriscore_messages()
            else: 
                self.substitute.get_an_other_substitute()
                if self.substitute.last_substitute:
                    self.user_interface.print_no_better_substitute_message()
                else:
                    self.user_interface.show_an_other_substitute(self.substitute.substitute_id)
            self.__select_an_option()
        else: 
            self.__launch_program()

    def __add_to_favorite(self, substitute_id):
        """
        Add a product to the Favorite table 

        Parameters
        -------
        substitute_id: int

        """
        self.methods_for_db.insert_product_to_favorites(substitute_id)
        self.user_interface.print_favorite_added_message()

    def __go_back_to_menu(self):
        """
        Go back to the menu section

        """
        self.user_interface.go_back_to_menu()
        if self.user_interface.action == 'y':
            self.__launch_program()
        else:
            self.user_interface.print_goodbye_message()
            sys.exit()