from flask import render_template
from flask.views import MethodView
import gbmodel


class Index(MethodView):
    """ grab the entries and set the type of model """	
    def get(self):
        model = gbmodel.get_model()
        # generate a list of dicts containing entries
        entries = [dict(name=row[0], species=row[1], breed=row[2], age=row[3], sex=row[4], traits=row[5], image=row[6]) for row in model.select()]
        return render_template('index.html', entries=entries)
