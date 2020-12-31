import peewee as p
from . import config

class Methods:
	def __init__(self, database):
		self.database = database

	def insert_in_product_table(self, product):
		self.database.Product.insert(name = product['name'], 
					brand = product['brand'],
					description = product['description'],
					shop = product['stores'],
					link = product['url'], 
					nutriscore = product['nutriscore']
					 ).execute()

	def insert_in_category_table(self, category):
		self.database.Category.insert(name = category).execute()

	def insert_categorized_to_database(self, cleaned_product):
		product = self.database.Product.get(name = cleaned_product['name'])
		category_names = cleaned_product['categories']
		for category_name in category_names:
			category = self.database.Category.get(name = category_name)
			self.database.Categorized.insert(product = product, category = category).execute()

	def insert_product_to_favorites(self, product_id):
		self.database.Favorite.insert(product = product_id).execute()

	def get_a_category(self, category_id):
		return self.database.Category.get_by_id(category_id)

	def get_category_length(self, category_id):
		return len(self.database.Categorized.select().where(self.database.Categorized.category == category_id))	

	def get_a_product(self, product_id):
		return self.database.Product.get_by_id(product_id)	

	def get_products_from_a_category(self, category_id):
		return self.database.Product.select().join(self.database.Categorized).where(self.database.Categorized.category == category_id)

	def get_categories_from_a_product(self, product_id):
		return self.database.Category.select().join(self.database.Categorized).where(self.database.Categorized.product == product_id)

	def get_favorites_products(self):
		query = self.database.Favorite.select()
		self.favorites = [self.get_a_product(self.database.Favorite.get_by_id(favorite).product_id) for favorite in query]	


			

