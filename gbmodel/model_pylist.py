from .Model import Model

# Derived class that implements Model using python lists.
class model(Model):
    """ Initializes null list """
    def __init__(self):
	# set an entry as a null list.
        self.bubble_entry = []

    """ Return current list """
    def select(self):
	# return self.
        return self.bubble_entry

    """Append list containing name, street_address, city, state, zip_code, store_hours, 
       phone_number, rating, review, and drink_order to bubble_entry list """
    def insert(self, name, street_address, city, state, zip_code, store_hours, phone_number, rating, review, drink_order):
        params = [name, street_address, city, state, zip_code, store_hours, phone_number, rating, review, drink_order]
	# append new entry onto itself.
        self.bubble_entry.append(params)
        return True
