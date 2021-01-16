from tqdm import tqdm


class Saver:
    """
    A class that save in a database the cleaned data

    Methods
    -------
    __add_product_to_database(self, product)
        Call a method in our database package to add a product to our database product table

    __add_category_to_database(self, category)
        Call a method in our database package to add a category to our database category table

    __add_clean_product_to_database(self, product)
        Call a method in our database package to add a categorized element to our database categorized table
    """

    def __init__(self, cleaned_data, methods_for_db):
        """
        Parameters
        -------
        cleaned_data: instance of Cleaner class
        methods_for_db: instance of Methods class from database package
        """

        self.cleaned_data = cleaned_data
        self.methods_for_db = methods_for_db
        print("Creation of the Product table")
        for product in tqdm(self.cleaned_data.cleaned_products_sorted):
            self.__add_product_to_database(product)
        print("Creation of the Category table")
        for category in tqdm(self.cleaned_data.category_names_sorted):
            self.__add_category_to_database(category)
        print("Creation of the Categorized table")
        for product in tqdm(self.cleaned_data.cleaned_products_sorted):
            self.__add_categorized_element_to_database(product)

    def __add_product_to_database(self, product):
        """
        Call a method in /database to add a product to our database product table

        Parameters
        -------
        product: dict
            Dict with well selected data: product = {'name' = x, 'brand' = y, categories = [a, b, c]...}

        """
        self.methods_for_db.get_or_create_in_product_table(product)

    def __add_category_to_database(self, category):
        """
        Call a method in /database to add a category to our database category table

        Parameters
        -------
        category: str
            element of a list of categories
        """
        self.methods_for_db.get_or_create_in_category_table(category)

    def __add_categorized_element_to_database(self, product):
        """
        Call a method in /database to add a cateoprized element to our database categorized table

        Parameters
        -------
        product: dict
            Dict with well selected data: product = {'name' = x, 'brand' = y, categories = [a, b, c]...}
        """
        self.methods_for_db.get_or_create_categorized_to_database(product)
