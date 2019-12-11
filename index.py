from flask import render_template
from flask.views import MethodView
import gbmodel
import dog_api as dog
import cat_api as cat


class Index(MethodView):
    """ grab the entries and set the type of model """	
    def get(self):
        model = gbmodel.get_model()
        dog_list = dog.master_breeds()
        cat_list = cat.master_breeds()
        # generate a list of dicts containing entries
        entries = [dict(name=row[0], species=row[1], breed=row[2], age=row[3], sex=row[4], traits=row[5], image=row[6], fact=row[7] ) for row in model.select()]
        num_entry = len(entries)
        return render_template('index.html', entries=entries, num_entry=num_entry, dog_list=dog_list, cat_list=cat_list)
