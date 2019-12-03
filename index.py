from flask import render_template
from flask.views import MethodView
import gbmodel


class Index(MethodView):
    """ grab the entries and set the type of model """	
    def get(self):
        model = gbmodel.get_model()
        # generate a list of dicts containing entries
        entries = [dict(name=row[0], street_address=row[1], city=row[2], state=row[3], zip_code=row[4], store_hours=row[5],
                        phone_number=row[6], rating=row[7], review=row[8], drink_order=row[9]) for row in model.select()]
        return render_template('index.html', entries=entries)
