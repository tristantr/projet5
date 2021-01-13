from api import downloader
from api import cleaner
from api import saver
from database import config
from database import methods
from application import user_section
from application import menu_section
from application import substitution_algo
from application import global_section

def main():
	downloaded_data = downloader.Downloader()
	cleaned_data = cleaner.Cleaner(downloaded_data)
	database = config.Database()
	methods_for_db = methods.Methods(database)

	saved_data = saver.Saver(cleaned_data, methods_for_db)
	menu_interface = menu_section.Menu()
	substitute = substitution_algo.Substitution(methods_for_db)		
	# user_interface = user_section.User_interface(cleaned_data, methods_for_db)
	user_interface = user_section.User_interface(cleaned_data, methods_for_db)


	# substitute = substitution_algo.Substitution(methods_for_db, user_interface.id_of_the_product_to_substitute, user_interface.selected_category_id)

	global_interface = global_section.Global_section(menu_interface, user_interface, methods_for_db, substitute)	

	
if __name__ == '__main__':
    main()    

#######################

# def main():
# 	downloaded_data = downloader.Downloader()
# 	cleaned_data = cleaner.Cleaner(downloaded_data)
# 	database = config.Database()
# 	methods_for_db = methods.Methods(database)
# 	substitute = substitution_algo.Substitution(methods_for_db)
# 	saved_data = saver.Saver(cleaned_data, methods_for_db)
# 	menu_interface = menu_section.Menu()
# 	user_interface = user_section.User_interface(cleaned_data, methods_for_db, substitute)



# 	global_interface = global_section.Global_section(menu_interface, user_interface, methods_for_db, substitute)	

	
# if __name__ == '__main__':
#     main()        