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
    def insert(self, name, type, breed, age, sex, traits, image):
        """
        Inserts entry into database
        :param name: String
        :param type: String
        :param breed: String
	:param age: Integer
        :param sex: String
        :param traits: String
        :param image: image
        :return: none
        :raises: Database errors on connection and insrtion
        """
        pass



