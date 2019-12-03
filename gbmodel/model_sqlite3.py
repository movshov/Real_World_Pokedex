"""
A simple bobba store flask app.
data is stored in a SQLite database.
"""
from .Model import Model
import sqlite3
DB_FILE = 'bobba.db'    # file for our Database


class model(Model):
    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
	# try to count the number of rows in the table.
        try:
            cursor.execute("select count(rowid) from bobbabook")
	# if we get an error we know the table doesn't exist yet.
        except sqlite3.OperationalError:
	    # create a new table "bobbabook" with these columns
            cursor.execute(
                "create table bobbabook (name text, street_address text, city text, state text, zip_code text, store_hours text, phone_number text, rating text, review text, drink_order text)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: name, street_address, city, state, zip_code, store_hours
        phone_number, rating, review, and drink_order
        :return: List of lists containing all rows of database
        """
	# connect to the database "bobba.db"
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
	# grab everything from the table.
        cursor.execute("SELECT * FROM bobbabook")
	# return everything we have gotten.
        return cursor.fetchall()

    def insert(self, name, street_address, city, state, zip_code, store_hours, phone_number, rating, review, drink_order):
        """
        Inserts entry into database
        :param name: String
        :param street_address: String
        :param city: String
        :param state: String
        :param zip_code: Integer
        :param store_hours: String
        :param phone_number: String
        :param rating: Integer
        :param review: String
        :param drink_order: String
        :return: none
        :raises: Database errors on connection and insrtion
        """
	# set the params.
        params = {'name': name, 'street_address': street_address, 'city': city, 'state': state, 'zip_code': zip_code,
                  'store_hours': store_hours, 'phone_number': phone_number, 'rating': rating, 'review': review, 'drink_order': drink_order}
	# connect to the database "bobba.db"
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
	# insert params into the table "bobbabook"
        cursor.execute("insert into bobbabook (name, street_address, city, state, zip_code, store_hours, phone_number, rating, review, drink_order) VALUES (:name, :street_address, :city, :state, :zip_code, :store_hours, :phone_number, :rating, :review, :drink_order)", params)

        connection.commit()
        cursor.close()
        return True
