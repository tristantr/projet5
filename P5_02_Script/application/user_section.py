import random


class User_interface:
    """
    Class that creates the user interface

    Methods
    -------
    display_categories(self)
        Display categories from Category table

    display_favorites(self)
        Display favorites from Favorite table

    select_category(self)
        Select the category of the product we want to substitute

    display_products_from_selected_category(self, selected_category_id)
        Display the products of the selected category

    select_a_product(self, selected_category_id)
        Select the product we want to substitute

    select_header(self, sentence)
        Define a header

    show_selected_product_informations(self, product)
        Call methods to show informations of the product we want to substitute

    show_product_informations(self, product)
        Show product information

    show_a_substitute(self, products_by_number_of_common_categories, sorted_number_of_common_category)
        Show a substitute for the product we selected

    get_an_other_substitute(self, products_by_number_of_common_categories, sorted_number_of_common_category)
        Ask for an other substitute if not satisfied

    """

    def __init__(self, cleaned_data, methods_for_db):
        """
        Parameters
        -------
        cleaned_data: instance of the Cleaner class in api package

        methods_for_db: instance of Methods class in database package

        substitute: instance of Substitution class

        """

        self.cleaned_data = cleaned_data
        self.methods_for_db = methods_for_db
        self.total_number_of_categories = range(
            1, len(self.cleaned_data.category_names_sorted) + 1
        )
        maximum_number_of_elements = 35
        categories_for_substitution_program = []
        for category_id in self.total_number_of_categories:
            if self.methods_for_db.get_category_length(category_id) > 10:
                categories_for_substitution_program.append(category_id)
        self.restricted_number_of_categories = sorted(
            random.sample(
                categories_for_substitution_program, maximum_number_of_elements
            )
        )

        self.messages = {
            "favorites": "The product has been added to your favorites! ",
            "best_nutriscore": "Your product has the best nutriscore of its category!",
            "goodbye": "Thanks for using our program, have a nice day !",
            "no_favorites": "Your list of favorites is empty!",
            "back_menu": "Go back to the menu (y/n)? ",
            "which_action": "Which action do you want to make? ",
            "perfect_substitute": "Here is the perfect substitute with a better nutriscore!",
            "-": "---------------------------------------------------------",
            "skip_a_lign": "",
            "best_substitute": "There is no better substitute for this product!",
            "category_value_error": "Select a category_number: ",
            "category_assertion_error": "The category you chose doesn't exist ! ",
            "product_value_error": "Select a product number ! ",
            "product_assertion_error": "The product you chose doesn't exist ! ",
            "option_value_error": "Select an action number ! ",
            "option_assertion_error": "The action you chose doesn't exist ! ",
            "option_assertion_error_2": "The action you chose doesn't exist ! Select a valid action :  ",
        }

    def display_user_interface(self):
        """
        Generate the user interface
        """
        self.display_categories()
        self.select_category()
        self.display_products_from_selected_category()
        self.select_a_product()
        self.show_selected_product_informations()

    def display_categories(self):
        """
        Display categories from Category table
        """
        for category_position, category_id in enumerate(
            self.restricted_number_of_categories
        ):
            category_name = self.methods_for_db.get_a_category(category_id).name
            print("{} : {}".format(category_position + 1, category_name))

    def display_favorites(self):
        """
        Display favorites from Favorite table
        """
        self.methods_for_db.get_favorites_products()
        sentence_for_favorites = "your favorite products!"
        if self.methods_for_db.favorites == []:
            print(self.messages["skip_a_lign"])
            print(self.messages["-"])
            print(self.messages["no_favorites"])
            print(self.messages["-"])
        else:
            self.select_header(sentence_for_favorites)
            for favorite_id, favorite in enumerate(self.methods_for_db.favorites):
                print("{}".format(favorite_id + 1))
                self.show_product_informations(favorite)

    def select_category(self):
        """
        Select the category of the product we want to substitute
        """
        print(self.messages["skip_a_lign"])

        while True:
            try:
                category = int(input("Select a category: "))
                print(self.messages["skip_a_lign"])
                assert 0 < category < len(self.restricted_number_of_categories) + 1
            except ValueError:
                print(self.messages["skip_a_lign"])
                print(self.messages["category_value_error"])
            except AssertionError:
                print(self.messages["skip_a_lign"])
                print(self.messages["category_assertion_error"])
            else:
                break

        self.selected_category_id = list(
            enumerate(self.restricted_number_of_categories)
        )[category - 1][1]

    def display_products_from_selected_category(self):
        """
        Display the products of the selected category

        Parameters
        -------
        selected_category_id: int

        """
        self.products_from_category = self.methods_for_db.get_products_from_a_category(
            self.selected_category_id
        )
        for product_position, product_id in enumerate(self.products_from_category):
            product_name = self.methods_for_db.get_a_product(product_id).name
            print("{} : {}".format(product_position + 1, product_name))

    def select_a_product(self):
        """
        Select the product we want to substitute

        Parameters
        -------
        selected_category_id: int

        """

        category_length = self.methods_for_db.get_category_length(
            self.selected_category_id
        )
        print(self.messages["skip_a_lign"])

        while True:
            try:
                product = int(input("Select a product: "))
                print(self.messages["skip_a_lign"])
                assert 0 < product < category_length + 1
            except ValueError:
                print(self.messages["skip_a_lign"])
                print(self.messages["product_value_error"])
            except AssertionError:
                print(self.messages["skip_a_lign"])
                print(self.messages["product_assertion_error"])
            else:
                break

        self.id_of_the_product_to_substitute = list(
            enumerate(self.products_from_category)
        )[product - 1][1]

    def select_header(self, sentence):
        """
        Define a header

        Parameters
        -------
        sentence: str

        """
        print(self.messages["skip_a_lign"])
        print("Here is information about {} ".format(sentence))
        print(self.messages["-"])

    def show_selected_product_informations(self):
        """
        Call methods to show informations of the product we want to substitute
        """
        sentence = "the product you chose ! "
        self.select_header(sentence)
        self.show_product_informations(self.id_of_the_product_to_substitute)

    def show_product_informations(self, product):
        """
        Show product information

        Parameters
        -------
        product: int

        """
        print("Product name: {}".format(product.name))
        print("Brand : {}".format(product.brand))
        print("Nutriscore : {}".format(product.nutriscore))
        print("Shops: {}".format(product.shop))
        print("URL: {}".format(product.link))
        print(self.messages["-"])

    def show_a_substitute(self, substitute_id):
        """
        Show substitute information

        Parameters
        -------
        substitute_id: int

        """
        substitute = self.methods_for_db.get_a_product(substitute_id)
        print(self.messages["perfect_substitute"])
        print(self.messages["-"])
        print("Product name: {}".format(substitute.name))
        print("Brand : {}".format(substitute.brand))
        print("Nutriscore : {}".format(substitute.nutriscore))
        print("Shops: {}".format(substitute.shop))
        print("URL: {}".format(substitute.link))
        print(self.messages["-"])

    def show_an_other_substitute(self, substitute_id):
        """
        Header for an other substitute information

        Parameters
        -------
        substitute_id: int

        """
        sentence = "an other possible substitute! "
        self.select_header(sentence)
        self.show_product_informations(substitute_id)

    def select_an_option(self):
        """
        Select the next action you want to make.
        """
        options = ["Add to favorites", "Get an other substitute", "Go back to menu"]
        number_of_options = len(options)

        for option_position, option in enumerate(options):
            print("{}: {}".format(option_position + 1, option))
            print(self.messages["skip_a_lign"])

        while True:
            try:
                self.selected_option = int(input(self.messages["which_action"]))
                print(self.messages["skip_a_lign"])
                assert 0 < self.selected_option < number_of_options + 1
            except ValueError:
                print(self.messages["skip_a_lign"])
                print(self.messages["option_value_error"])
            except AssertionError:
                print(self.messages["skip_a_lign"])
                print(self.messages["option_assertion_error"])
            else:
                break

    def go_back_to_menu(self):
        """
        Go back to menu
        """
        self.action = input(self.messages["back_menu"])
        while self.action not in ["y", "n"]:
            self.action = input(self.messages["option_assertion_error_2"])

    def print_best_nutriscore_messages(self):
        """
        Display a specific message when you get the product with the best nutriscore of its category.
        """
        print(self.messages["skip_a_lign"])
        print(self.messages["best_nutriscore"])
        print(self.messages["skip_a_lign"])

    def print_favorite_added_message(self):
        """
        Display a specific message when a product has been added to the Favorites.
        """
        print(self.messages["skip_a_lign"])
        print(self.messages["favorites"])
        print(self.messages["skip_a_lign"])

    def print_goodbye_message(self):
        """
        Display a message when the user leaves the program.
        """
        print(self.messages["skip_a_lign"])
        print(self.messages["goodbye"])
        print(self.messages["skip_a_lign"])

    def print_no_better_substitute_message(self):
        """
        Display a specific message there is no better substitute available.
        """
        print(self.messages["-"])
        print(self.messages["best_substitute"])
        print(self.messages["-"])
