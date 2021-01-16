import mysql.connector
import peewee as p
from dotenv import load_dotenv
import os

load_dotenv()

myDB = p.MySQLDatabase(
    "Projet_5",
    host=os.getenv("HOST"),
    user=os.getenv("USER"),
    passwd=os.getenv("PASSWORD"),
)


class Database_model(p.Model):
    """
    A class that represents our database model
    """

    class Meta:
        database = myDB


class Product(Database_model):
    """
    A class that configures the Product table
    """

    product_id = p.AutoField(primary_key=True, unique=True)
    name = p.CharField()
    brand = p.CharField()
    description = p.CharField()
    shop = p.CharField()
    link = p.CharField()
    nutriscore = p.FixedCharField(1)


class Category(Database_model):
    """
    A class that configures the Category table
    """

    category_id = p.AutoField(primary_key=True, unique=True)
    name = p.CharField()


class Categorized(Database_model):
    """
    A class that configures the Categorized table
    """

    categorized_id = p.AutoField(primary_key=True, unique=True)
    product = p.ForeignKeyField(Product, backref="categories")
    category = p.ForeignKeyField(Category, backref="products")


class Favorite(Database_model):
    """
    A class that configures the Favorite table
    """

    favorite_id = p.AutoField(primary_key=True, unique=True)
    product = p.ForeignKeyField(Product, backref="favorites")


class Database:
    """
    A class that configures the database

    Methods
    -------
    __configure_database(self)
        Connect to MySQL Connector and configure the database we will use for our program

    __create_tables(self)
        Create our database tables

    __create_new_database(self, mycursor):
        Method to drop the existaing database and create a new one

    """

    def __init__(self):
        self.__configure_db()

    def __configure_db(self):
        """
        Connect to MySQL Connector and configure the database we will use for our program
        Depending on the user choice, create a update the database

        """

        db = mysql.connector.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            passwd=os.getenv("PASSWORD"),
        )

        mycursor = db.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS Projet_5")


        options = ["Create a new database", "Update existing database"]
        for option_position, option in enumerate(options):
            print("")
            print("{}: {}".format(option_position + 1, option))
            print("")

        while True:
            try:
                selected_option = int(input("Which action do you want to make? "))
                print("")
                assert 0 < selected_option < 3
            except ValueError:
                print("")
                print("Select an action number !")
            except AssertionError:
                print("")
                print("The action you chose doesn't exist !")
            else:
                break

        if selected_option == 1:
            self.__create_new_database(mycursor)
            self.__create_tables()
        else:
            self.__create_tables()

    def __create_tables(self):
        """
        Create our database tables

        """
        self.Product = Product
        self.Category = Category
        self.Categorized = Categorized
        self.Favorite = Favorite
        myDB.connect()
        myDB.create_tables(
            [self.Product, self.Category, self.Categorized, self.Favorite], safe=True
        )

    def __create_new_database(self, mycursor):
        """
        Drop the existing database and create a new one

        Parameters
        -------
        mycursor: method
        """

        mycursor.execute("DROP DATABASE IF EXISTS Projet_5")
        mycursor.execute("CREATE DATABASE IF NOT EXISTS Projet_5")
