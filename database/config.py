import mysql.connector
import peewee as p

myDB = p.MySQLDatabase(
		"Projet_5",
		host = "localhost",
		user = "root",
		passwd = "Tristan92"
		)	

class Database_model(p.Model):
	class Meta:
		database = myDB

class Product(Database_model):
	product_id = p.AutoField(primary_key = True, unique = True)
	name = p.CharField() 
	brand = p.CharField()
	description = p.CharField()
	shop = p.CharField()
	link = p.CharField()
	nutriscore = p.FixedCharField(1)

class Category(Database_model):
	category_id = p.AutoField(primary_key = True, unique = True)
	name = p.CharField()

class Categorized(Database_model):
	categorized_id = p.AutoField(primary_key = True, unique = True)
	product = p.ForeignKeyField(Product, backref = 'categories')
	category = p.ForeignKeyField(Category, backref = 'products')

class Favorite(Database_model):
	favorite_id = p.AutoField(primary_key = True, unique = True)
	product = p.ForeignKeyField(Product, backref = 'favorites')		

class Database:
	def __init__(self):
		self.__configure_db()

	def __configure_db(self):
		db = mysql.connector.connect(
		host = "localhost",
		user = "root",
		passwd = "Tristan92",
		database = "Projet_5" 
		)

		mycursor = db.cursor()
		mycursor.execute("DROP DATABASE IF EXISTS Projet_5")
		mycursor.execute("CREATE DATABASE IF NOT EXISTS Projet_5")	

		self.__create_db()

	def __create_db(self):
		self.Product = Product
		self.Category = Category
		self.Categorized = Categorized
		self.Favorite = Favorite
		myDB.connect()
		myDB.create_tables([self.Product, self.Category, self.Categorized, self.Favorite], safe = True)