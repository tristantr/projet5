import sys

class Global_section():
	def __init__(self, menu_interface, user_interface, methods_for_db, substitute):
		self.menu_interface = menu_interface 
		self.user_interface = user_interface
		self.methods_for_db = methods_for_db
		self.substitute = substitute
		self.__launch_program(self.menu_interface)

	def __launch_program(self, menu_interface):
		self.menu_interface.display_home_screen()
		if self.menu_interface.selected_option == 1:
			self.__launch_substitution_program()
			self.__select_an_option()
		else:		
			self.user_interface.display_favorites()
			self.__go_back_to_menu()

	def __launch_substitution_program(self):
			self.user_interface.display_categories()
			self.user_interface.select_category()
			self.user_interface.display_products_from_selected_category(self.user_interface.selected_category_id)
			self.user_interface.select_a_product(self.user_interface.selected_category_id)
			self.user_interface.show_selected_product_informations(self.user_interface.id_of_the_product_to_substitute)
			self.substitute.get_a_substitute(self.user_interface.id_of_the_product_to_substitute, self.user_interface.selected_category_id)
			if self.substitute.products_with_better_nutriscores == []:
				print('')
				print('')
				print('Your product has the best nutriscore of its category!')
				print('')
				print('')
				self.user_interface.substitute_id = self.user_interface.id_of_the_product_to_substitute
			else: 	
				self.user_interface.show_a_substitute(self.user_interface.substitute.products_by_number_of_common_categories, self.user_interface.substitute.sorted_number_of_common_category)

	def __select_an_option(self):	
		options = ['Add to favorites', 'Go back to menu']
		number_of_options = len(options)

		for option_position, option in enumerate(options):
			print('{}: {}'.format(option_position + 1, option))
			print('')

		selected_option = int(input('Which action do you want to make? '))

		while selected_option not in [1, 2] :
			print('')
			selected_option = int(input("The action you chose doesn't exist. Please chose a valid action: "))
		if selected_option == 1:
			self.__add_to_favorite(self.user_interface.substitute_id)
			self.__go_back_to_menu()			
		else: 
			self.__launch_program(self.menu_interface)
				

	def __add_to_favorite(self, substitute_id):
		self.methods_for_db.insert_product_to_favorites(substitute_id)
		print('')
		print('The product has been added to your favorites! ')

	def __go_back_to_menu(self):
			print('')
			action = input("Go back to the menu (y/n)? ")
			while action not in ['y', 'n']:
				action = input("Please chose a valid option: ")
			if action == 'y':
				self.__launch_program(self.menu_interface)
			else: 
				print('')
				print('Thanks for using our program, have a nice day !')
				print('')
				sys.exit()		
