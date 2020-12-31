import random

class User_interface:
	def __init__(self, cleaned_data, methods_for_db, substitute):
		self.cleaned_data = cleaned_data
		self.methods_for_db = methods_for_db
		self.substitute = substitute
		self.total_number_of_categories = range(1, len(self.cleaned_data.category_names_sorted)+1)
		maximum_number_of_elements = 35
		categories_for_substitution_program = []
		for category_id in self.total_number_of_categories:
			if self.methods_for_db.get_category_length(category_id) > 10:
				categories_for_substitution_program.append(category_id)		
		self.restricted_number_of_categories = sorted(random.sample(categories_for_substitution_program, maximum_number_of_elements))

	def display_categories(self):
		for category_position, category_id in enumerate(self.restricted_number_of_categories):
			category_name = self.methods_for_db.get_a_category(category_id).name
			print('{} : {}'.format(category_position + 1, category_name))

	def display_favorites(self):
		self.methods_for_db.get_favorites_products()
		sentence_for_favorites = 'your favorite products !'
		if self.methods_for_db.favorites == []:
			print('')
			print('---------------------------------------------------------')
			print('Your list of favorites is empty! ')
			print('---------------------------------------------------------')
		else:
			self.select_header(sentence_for_favorites) 	
			for favorite_id, favorite in enumerate(self.methods_for_db.favorites):
				print('{}'.format(favorite_id + 1))
				self.show_product_informations(favorite)
					
	def select_category(self):
		print('')
		category = int(input('Select a category: '))
		while category not in range(1, len(self.restricted_number_of_categories) + 1):
			print('')
			category = int(input('Select a valid category: '))
		self.selected_category_id = list(enumerate(self.restricted_number_of_categories))[category - 1][1]	

	def display_products_from_selected_category(self, selected_category_id):
		self.products_from_category = self.methods_for_db.get_products_from_a_category(selected_category_id)
		for product_position, product_id in enumerate(self.products_from_category):
			product_name = self.methods_for_db.get_a_product(product_id).name
			print('{} : {}'.format(product_position + 1, product_name))

	def select_a_product(self, selected_category_id):
		category_length = self.methods_for_db.get_category_length(selected_category_id)
		category_choices = range(1, category_length + 1)
		print('')
		product = int(input('Select a product: '))
		while product not in category_choices:
			print('')
			product = int(input('Select a valid product: '))			
		self.id_of_the_product_to_substitute = list(enumerate(self.products_from_category))[product - 1][1]

	def select_header(self, sentence):
		print('')		
		print('Here is information about {} '.format(sentence))
		print('---------------------------------------------------------')

	def show_selected_product_informations(self, product):
		sentence = 'the product you chose ! '
		product = self.methods_for_db.get_a_product(product)
		self.select_header(sentence)
		self.show_product_informations(product)	
		

	def show_product_informations(self, product):
		print('Product name: {}'.format(product.name))
		print('Brand : {}'.format(product.brand))
		print('Nutriscore : {}'.format(product.nutriscore))
		print('Shops: {}'.format(product.shop))
		print('URL: {}'.format(product.link))
		print('---------------------------------------------------------')


	def show_a_substitute(self, products_by_number_of_common_categories, sorted_number_of_common_category):
		self.substitute_id = products_by_number_of_common_categories[sorted_number_of_common_category[0]][0]
		substitute = self.methods_for_db.get_a_product(self.substitute_id)

		print('Here is the perfect substitute with a better nutriscore!')
		print('---------------------------------------------------------')
		print('Product name: {}'.format(substitute.name))
		print('Brand : {}'.format(substitute.brand))
		print('Nutriscore : {}'.format(substitute.nutriscore))
		print('Shops: {}'.format(substitute.shop))
		print('URL: {}'.format(substitute.link))
		print('---------------------------------------------------------')


	# def __show_a_substitute(self, products_by_number_of_common_categories, sorted_number_of_common_category):
	# 	unapproved_substitute = True 
	# 	while unapproved_substitute:
	# 		for number in sorted_number_of_common_category:
	# 			for product in products_by_number_of_common_categories[number]:
	# 				product = self.methods_for_db.get_a_product(product)
	# 				print('')
	# 				print('Here is the perfect substitute with a better nutriscore!')
	# 				print('')
	# 				print('Product name: {}'.format(product.name))
	# 				print('Brand : {}'.format(product.brand))
	# 				print('Nutriscore : {}'.format(product.nutriscore))
	# 				print('Shops: {}'.format(product.shop))
	# 				print('URL: {}'.format(product.link))				
	# 				answer = input('Do you want an other subtitute ? (y/n): ')
	# 				if answer == 'n':
	# 					unapproved_substitute = False

	# 				# while answer != 'y':
	# 				# 	while answer != 'n':
	# 				# 		new_answer = input('Select a valid option (y/n): ')
	# 				# 		if new_answer == 'n':
	# 				# 			answer == 'n'
	# 				# 		elif new_answer == 'y':
	# 				# 			answer == 'y'	
	# 	self.__add_to_favorite_menu(product)











		
