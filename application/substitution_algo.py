class Substitution:
	def __init__(self, methods_for_db):
		self.methods_for_db = methods_for_db

	def get_a_substitute(self, id_of_the_product_to_substitute, category_of_the_product_to_substitute):
		products = self.methods_for_db.get_products_from_a_category(category_of_the_product_to_substitute)
		categories = self.methods_for_db.get_categories_from_a_product(id_of_the_product_to_substitute)

		products_from_selected_category = []
		categories_from_selected_product = []
		
		for product in products:
			products_from_selected_category.append(product)
		products_from_selected_category.remove(id_of_the_product_to_substitute)
		
		for category in categories:
			categories_from_selected_product.append(category)

		self.__get_products_with_better_nutriscores(products_from_selected_category, id_of_the_product_to_substitute)
		self.__sort_products_by_number_of_common_categories(self.products_with_better_nutriscores, categories_from_selected_product)


	def __get_products_with_better_nutriscores(self, products_from_selected_category, id_of_the_product_to_substitute):
		self.products_with_better_nutriscores = []
		nutriscore_of_the_product_to_substitute = self.methods_for_db.get_a_product(id_of_the_product_to_substitute).nutriscore
		nutriscores = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
		for product in products_from_selected_category:
			product_nutriscore = self.methods_for_db.get_a_product(product).nutriscore
			if nutriscores[product_nutriscore] < nutriscores[nutriscore_of_the_product_to_substitute]:
				self.products_with_better_nutriscores.append(product)

	def __sort_products_by_number_of_common_categories(self, products_with_better_nutriscores, categories_from_selected_product):
		self.products_by_number_of_common_categories = {}
		number_of_common_categories_keys = list(self.products_by_number_of_common_categories.keys())

		for product in products_with_better_nutriscores:
			product_dict = {}
			number_of_common_categories = 0
			categories = self.methods_for_db.get_categories_from_a_product(product)
			for category in categories:
				if category in categories_from_selected_product:
					number_of_common_categories += 1
			product_dict[number_of_common_categories] = [product]
	
			if number_of_common_categories not in number_of_common_categories_keys:
				self.products_by_number_of_common_categories.update(product_dict)
				number_of_common_categories_keys.append(number_of_common_categories)
			else:
				self.products_by_number_of_common_categories[number_of_common_categories].append(product)	

		self.sorted_number_of_common_category = sorted(number_of_common_categories_keys, reverse = True)

