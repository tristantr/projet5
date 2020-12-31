class Cleaner: 
	def __init__(self, downloaded_data):
		self.downloaded_data = downloaded_data
		self.category_names = []		
		self.cleaned_products = []
		self.product_names = []
		self.__check_products(downloaded_data)
		self.category_names_sorted = sorted(self.category_names)
		self.cleaned_products_sorted = sorted(self.cleaned_products, key = lambda i: i['name'])

	def __check_products(self, downloaded_data):
		for product in downloaded_data.products:
			if product.get('product_name') and product.get('brands') and product.get('categories') and product.get('stores') \
				and product.get('code') and product.get('nutriscore_grade') and product.get('ingredients_text'): 
				if product['product_name'] not in self.product_names:
					self.__format_categories_attribute_from_json_object(product)

	def __format_categories_attribute_from_json_object(self, product):
		self.product_categories = []
		lowered_categories = product['categories'].lower().split(', ' and ',')
		for category in lowered_categories:
			striped_category = category.strip()
			if striped_category.startswith('en') or striped_category.startswith('fr'):
				pass
			else:
				self.product_categories.append(striped_category)
				if striped_category not in self.category_names:
					self.category_names.append(striped_category)
		self.__set_product(product)			

	def __set_product(self, product):
		self.product_data = {}
		self.product_data['name'] = product['product_name'].lower()
		self.product_names.append(product['product_name'].lower())
		self.product_data['brand'] = product['brands']
		self.product_data['categories'] = self.product_categories
		self.product_data['description'] = product['ingredients_text']
		self.product_data['stores'] = product['stores']
		self.product_data['nutriscore'] = product['nutriscore_grade']
		self.product_data['url'] = 'https://fr.openfoodfacts.org/produit/{}'.format(product['code'])
		self.cleaned_products.append(self.product_data)
		self.product_data = {}