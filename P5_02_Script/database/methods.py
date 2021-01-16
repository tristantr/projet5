class Methods:
    """
    A class that defines our database related methods

    Methods
    -------
    get_or_create_in_product_table(self, product)
        When not existing, add a product to the Product table

    get_or_create_in_category_table(self, category)
        When not existing, add a category to the Category table

    get_or_create_categorized_to_database(self, product)
        When not existing, add a categorized element to the Categorized table

    insert_product_to_favorites(self, product_id)
        Insert a product in the Favorite table

    get_a_category(self, category_id):
        Returns a category object depending on its id

    get_category_length(self, category_id):
        Returns a category length depending on its id

    get_a_product(self, product_id):
        Returns a product object depending on its id

    get_products_from_a_category(self, category_id):
        Returns the list of products of a given category

    get_categories_from_a_product(self, product_id):
        Returns the list of categories for a given product

    get_favorites_products(self):
        Create a list of favorite elements
    """

    def __init__(self, database):
        self.database = database

    def get_or_create_in_product_table(self, product):
        """
        When not existing, add a product to the Product table

        Parameters
        -------
        product: dict {'name': name, 'brand': brand, 'description': description...}
        """

        self.database.Product.get_or_create(
            link=product["url"],
            defaults={
                "name": product["name"],
                "brand": product["brand"],
                "description": product["description"],
                "shop": product["stores"],
                "nutriscore": product["nutriscore"],
            },
        )

    def get_or_create_in_category_table(self, category):
        """
        When not existing, add a category to the Category table

        Parameters
        -------
        category: str
        """
        self.database.Category.get_or_create(name=category)

    def get_or_create_categorized_to_database(self, product):
        """
        When not existing, add a categorized element to the Categorized table

        Parameters
        -------
        product: dict {'name': name, 'brand': brand, 'description': description...}
        """

        product_name = self.database.Product.get(name=product["name"])
        category_names = product["categories"]
        for category_name in category_names:
            category = self.database.Category.get(name=category_name)
            self.database.Categorized.get_or_create(
                product=product_name, category=category
            )

    def insert_product_to_favorites(self, product_id):
        """
        Insert a product in the Favorite table

        Parameters
        -------
        product_id: int
        """

        self.database.Favorite.insert(product=product_id).execute()

    def get_a_category(self, category_id):
        """
        Returns a category object depending on its id

        Parameters
        -------
        category_id: int
        """

        return self.database.Category.get_by_id(category_id)

    def get_category_length(self, category_id):
        """
        Returns a category length depending on its id

        Parameters
        -------
        category_id: int
        """

        return len(
            self.database.Categorized.select().where(
                self.database.Categorized.category == category_id
            )
        )

    def get_a_product(self, product_id):
        """
        Returns a product object depending on its id

        Parameters
        -------
        product_id: int
        """

        return self.database.Product.get_by_id(product_id)

    def get_products_from_a_category(self, category_id):
        """
        Returns the list of products of a given category

        Parameters
        -------
        category_id: int
        """

        return (
            self.database.Product.select()
            .join(self.database.Categorized)
            .where(self.database.Categorized.category == category_id)
        )

    def get_categories_from_a_product(self, product_id):
        """
        Returns the list of categories for a given product

        Parameters
        -------
        product_id: int
        """

        return (
            self.database.Category.select()
            .join(self.database.Categorized)
            .where(self.database.Categorized.product == product_id)
        )

    def get_favorites_products(self):
        """
        Create a list of favorite elements
        """

        query = self.database.Favorite.select()
        self.favorites = [
            self.get_a_product(self.database.Favorite.get_by_id(favorite).product_id)
            for favorite in query
        ]
