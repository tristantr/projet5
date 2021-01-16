# Projet 5 - Get a healthier product with the OpenFoodFacts API

 * Introduction
 * Installation
 * Launch the program
 * Built with
 * Author

## INTRODUCTION

In this program, the user selects a category, chooses a product from this category and gets a healthier substitute with a better nutriscore. 
This program uses data from the public API OpenFoodFacts. 

### Installation

Create a directory called OpenFoodFacts

Execute the command ``git clone https://github.com/tristanttttr/projet5.git`` to get the project

Execute the commande ``cd OpenFoodFacts/`` to get into the directory

Install the virtualenv package to create a virtual environement with the command ``pip install virtualenv``

Create the virtual environment with ``virtualenv OpenFoodFacts``

Activate the virtual environment:

Mac OS / Linux : use the command ``source OpenFoodFacts/bin/activate``
Windows : use the command ``OpenFoodFacts\Scripts\activate``
You should see the name of your virtual environment in brackets on your terminal line.
To desactivate your virtual environment, use the command ``desactivate``

Install all required modules with ``pip install -r requirements.txt``

Create a dotenv document:
Open a .txt file and rename it .env: 

Copy and Past the following, replacing 'xxx' by your information :

HOST=xxx

USER=xxx

PASSWORD=xxx 

Save this .env file in the root directory of the project


## Launch the program 

To launch the program, execute the command ``python3 main.py``

## How to use 

Once on the Menu section, select the "Get a substitute" option and choose a category of the product you want to substitute. 

If you want to have a good substitute for cookies, select the "snacks" category. 
Then find your product, select it and the program will give you a better substitute with a better nutriscore. 
For each substitute, you will get the name, the brand, the description, the nutriscore, the product page in OpenFoodFacts and stores where to buy it.

If you are not convinced by the substitute, you can get an other one ! 
Juste select the "Get another substitute" option. 

You can add the substitute to your list of favorites, and have access to it whenever you want. 


## Built with

Here are some modules I used to build the program, all listed in the requirements.txt file.

 * __Requests__ (https://pypi.org/project/requests/)
 * __Tqdm__ (https://pypi.org/project/tqdm/)
 * __PyMySQL__ (https://pypi.org/project/PyMySQL/)
 * __MySQL Connector__ (https://dev.mysql.com/doc/connector-python/en/)
 * __Peewee__ (https://pypi.org/project/peewee/)
 * __Dotenv__ (https://www.npmjs.com/package/dotenv)

## Author

Tristan Ttttr (https://github.com/tristanttttr)
