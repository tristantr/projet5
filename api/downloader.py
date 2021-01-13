import requests
import sys

from tqdm import tqdm

class Downloader:

    """
    A class used to download data frrom public API OpenFoodFacts 

    Methods
    -------
    __get_data()
        Download data and create a products list
    """
    
    def __init__(self):
        """
        Parameters
        -------
        None
        """ 

        self.products = []
        self.__get_data()

    def __get_data(self):
        """
        Download data from OpenFoodFacts and fill a list of products with uncleaned data
        """
            
        number_of_pages = range(1,10)
        print('Data recovery from Openfoodfacts')   
        for i in tqdm(number_of_pages):
            payload = {'action': 'process', 'json': 'true', 'page': i, 'page_size': 50}
            try: 
                r = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', params = payload)    
                if not r.ok:
                    raise Exception
                else:   
                    r_json = r.json()
                    products_from_this_page = r_json['products']
                    self.products.extend(products_from_this_page)
            except Exception:
                print('ERROR: Your connexion has failed. Please try again')
                sys.exit(0)
