class Substitution:

    """
    Class that definies our substitution algorithm

    Methods
    -------
    launch_substitution_program(self, id_of_the_product_to_substitute, selected_category_id)
        Launch the substitution algorithm after chosing the product to substitute

    __get_products_from_a_category(self, id_of_the_product_to_substitute, selected_category_id)
        Get all the products from the selected category

    __get_categories_from_a_product(self, id_of_the_product_to_substitute)
        Get all the categories from the selected category

    __get_products_with_better_nutriscores(self, id_of_the_product_to_substitute)
        Create a list of product with better nutriscore than the selected product

    __sort_products_by_number_of_common_categories(self)
        Create a dict with number of common categories for keys and products as values
            {'1': [product A, product B], '3': [product D, product Z], ...}

    __get_a_substitute_id(self)
        Get the id of a good substitute

    get_an_other_substitute(self)
        Get the id of an other good substitute  
    """

    def __init__(self, methods_for_db):
        """
        Parameters
        -------
        methods_for_db: instance of Methods class in database package

        """     
        self.methods_for_db = methods_for_db


    def launch_substitution_program(self, id_of_the_product_to_substitute, selected_category_id):
        """
        Launch the substitution algorithm after chosing the product to substitute 

        Parameters
        -------
        id_of_the_product_to_substitute: int
        selected_category_id: int

        """            
        self.last_substitute = False        
        self.products_from_selected_category = []
        self.categories_from_selected_product = []        
        self.products_with_better_nutriscores = []        
        self.products_by_number_of_common_categories = {}
        self.__get_products_from_a_category(id_of_the_product_to_substitute, selected_category_id)
        self.__get_categories_from_a_product(id_of_the_product_to_substitute)
        self.__get_products_with_better_nutriscores(id_of_the_product_to_substitute)
        if self.products_with_better_nutriscores != []:
            self.__sort_products_by_number_of_common_categories()
            self.__get_a_substitute_id()
        else: 
            pass


    def __get_products_from_a_category(self, id_of_the_product_to_substitute, selected_category_id):
        """
        Get all the products from the selected category

        Parameters
        -------
        id_of_the_product_to_substitute: int
        selected_category_id: int
        """
        products = self.methods_for_db.get_products_from_a_category(selected_category_id)  
        for product in products:
            self.products_from_selected_category.append(product)
        self.products_from_selected_category.remove(id_of_the_product_to_substitute)

    def __get_categories_from_a_product(self, id_of_the_product_to_substitute):
        """
        Get all the categories from the selected category

        Parameters
        -------
        id_of_the_product_to_substitute: int
        """
        categories = self.methods_for_db.get_categories_from_a_product(id_of_the_product_to_substitute)
        for category in categories:
            self.categories_from_selected_product.append(category)

    def __get_products_with_better_nutriscores(self, id_of_the_product_to_substitute):
        """
        Create a list of product with better nutriscore than the selected product 
        
        Parameters
        -------
        id_of_the_product_to_substitute: int
        """
        nutriscore_of_the_product_to_substitute = self.methods_for_db.get_a_product(id_of_the_product_to_substitute).nutriscore
        nutriscores = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        for product in self.products_from_selected_category:
            product_nutriscore = self.methods_for_db.get_a_product(product).nutriscore
            if nutriscores[product_nutriscore] < nutriscores[nutriscore_of_the_product_to_substitute]:
                self.products_with_better_nutriscores.append(product)    



    def __sort_products_by_number_of_common_categories(self):
        """
        Create a dict with number of common categories for keys and products as values
            {'1': [product A, product B], '3': [product D, product Z], ...}
        """       
        number_of_common_categories_keys = list(self.products_by_number_of_common_categories.keys())

        for product in self.products_with_better_nutriscores:
            product_dict = {}
            number_of_common_categories = 0
            categories = self.methods_for_db.get_categories_from_a_product(product)
            for category in categories:
                if category in self.categories_from_selected_product:
                    number_of_common_categories += 1
            product_dict[number_of_common_categories] = [product]
    
            if number_of_common_categories not in number_of_common_categories_keys:
                self.products_by_number_of_common_categories.update(product_dict)
                number_of_common_categories_keys.append(number_of_common_categories)
            else:
                self.products_by_number_of_common_categories[number_of_common_categories].append(product)
        self.sorted_number_of_common_category = sorted(number_of_common_categories_keys, reverse = True)


    def __get_a_substitute_id(self):
        """
        Get the id of a good substitute 
        """
        self.category_rank = 0
        self.substitute_rank = 0
        if self.products_by_number_of_common_categories[self.sorted_number_of_common_category[self.category_rank]] != []:
            self.substitute_id = self.products_by_number_of_common_categories[self.sorted_number_of_common_category[self.category_rank]][self.substitute_rank]
        else: 
            self.print_no_better_substitute()

    def get_an_other_substitute(self):
        """
        Get the id of an other good substitute
        """        
        if len(self.products_by_number_of_common_categories[self.sorted_number_of_common_category[self.category_rank]]) > self.substitute_rank + 1:
            self.substitute_rank += 1
            self.substitute_id = self.products_by_number_of_common_categories[self.sorted_number_of_common_category[self.category_rank]][self.substitute_rank]
        elif len(self.sorted_number_of_common_category) > self.category_rank + 1:
            self.substitute_rank = 0
            self.category_rank += 1
            self.substitute_id = self.products_by_number_of_common_categories[self.sorted_number_of_common_category[self.category_rank]][self.substitute_rank]
        else: 
            self.last_substitute = True
        