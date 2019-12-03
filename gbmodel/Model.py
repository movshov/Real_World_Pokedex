# Base class for model.
class Model():
    # To return list containing all entries.
    def select(self):
        """
        Gets all entries from the database
        :return: Tupel containing all rows of database
        """
        pass
    # To insert a new entry.
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
        pass



