import requests
import sys


class Downloader:
	def __init__(self):
		self.categories = {}
		self._get_categories()
		self._get_data_from_selected_category()

	def _get_categories(self):	
		try:
			category_request_from_OFF = requests.get('https://fr.openfoodfacts.org/categories.json')
			if not category_request_from_OFF.ok:
				raise Exception
			else:
				formatted_category_request = category_request_from_OFF.json()
				all_categories = formatted_category_request['tags']
				i = 1
				for category in all_categories:
					if category['products'] > 6000:
						self.categories[i] = category['name']
						print('{}.{}'.format(i, category['name']))
						i += 1					
		except Exception:
			print('ERROR: Your connexion has failed. Please try again')
			sys.exit(0)

	def _get_data_from_selected_category(self):
		category_number = int(input("Select a category number: "))
		number_of_pages = range(1,5)
		product_id = 1
		self.product_data = {}
		self.products_cleaned = {}
			
		for i in number_of_pages:
			payload = {'page': i, 'page_size': 5}
			products_request = requests.get('https://fr.openfoodfacts.org/category/{}.json'.format(self.categories[category_number]), params = payload)		

			formatted_products_request = products_request.json()

			products_from_selected_category = formatted_products_request['products']

			for product in products_from_selected_category:	
				if 'product_name' in product:
					if 'nutriscore_grade' in product:
						self.product_data['name'] = product['product_name']
						self.product_data['nutriscore'] = product['nutriscore_grade']
						self.products_cleaned[product_id] = self.product_data
						self.product_data = {}
						product_id += 1	
		print(self.products_cleaned)

