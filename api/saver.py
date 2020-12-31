import mysql.connector
import peewee as p

from tqdm import tqdm

class Saver:
	def __init__(self, cleaned_data, methods_for_db):
		self.cleaned_data = cleaned_data
		self.methods_for_db = methods_for_db
		print('Creation of the Product table')
		for product in tqdm(self.cleaned_data.cleaned_products_sorted):
			self.__add_product_to_database(product)
		print('Creation of the Category table')	
		for category in tqdm(self.cleaned_data.category_names_sorted):
			self.__add_category_to_database(category)
		print('Creation of the Categorized table')	
		for clean_product in tqdm(self.cleaned_data.cleaned_products_sorted):
			self.__add_clean_product_to_database(clean_product)

	def __add_product_to_database(self, product):
		self.methods_for_db.insert_in_product_table(product)

	def __add_category_to_database(self, category):
		self.methods_for_db.insert_in_category_table(category)	
		
	def __add_clean_product_to_database(self, clean_product):
		self.methods_for_db.insert_categorized_to_database(clean_product)
