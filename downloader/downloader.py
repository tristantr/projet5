import requests
import sys


class Downloader:
	def __init__(self):
		self.categories_dict = {}
		self._get_categories()
		self._get_data_from_category()

	def _get_categories(self):	
		try:
			r0 = requests.get('https://fr.openfoodfacts.org/categories.json')
			if not r0.ok:
				raise Exception
			else:
				r0_dict = r0.json()
				categories = r0_dict['tags']
				i = 1
				for category in categories:
					if category['products'] > 5000:
						self.categories_dict[i] = category['name']
						print('{}.{}'.format(i, category['name']))
						i += 1				
		except Exception:
			print('ERREUR: Votre connexion a été interrompue. Veuillez réessayer dans quelques instants')
			sys.exit(0)

	def _get_data_from_category(self):
		try:
			category_number = int(input("Select a category number: "))
			if category_number not in self.categories_dict:
				raise Exception
			else:
				number_of_pages = range(1,10)
				j = 1
				for i in number_of_pages:
					payload = {'page': i, 'page_size': 10}
					r = requests.get('https://fr-en.openfoodfacts.org/category/{}.json'.format(self.categories_dict[category_number]), params = payload)		

					r_dict = r.json()
					r_products = r_dict['products']
			
					for product in r_products:
						if 'product_name' in product: 
							print("{}. {}".format(j, product['product_name']))
						else: 
							print("Le produit n'a pas de nom")
						j += 1
		except Exception:
			print("ERREUR: VEUILLEZ SELECTIONNER UNE CATEGORIE VALIDE")
			self._get_data_from_category()	


		# if 'nutriscore_grade' in product: # on vérifie que la clé existe en json
		# 	print("{}. {} : Nutriscore {}".format(j, product['product_name'], product['nutriscore_grade']))
		# else:
		# 	print("{}. {} : PAS DE NUTRISCORE".format(j, product['product_name']))	
		# j += 1	



