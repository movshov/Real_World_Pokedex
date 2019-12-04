from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel
import dog_api as dog

class Sign(MethodView):
    def get(self):
        return render_template('sign.html')
   
    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        rand_image = dog.random_image(request.form['breed'])
        print("rand_image is: \n", rand_image)
        model = gbmodel.get_model()
        model.insert(request.form['name'], request.form['species'], request.form['breed'], request.form['age'], request.form['sex'], request.form['traits'], rand_image)
        return redirect(url_for('index'))



