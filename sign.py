from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel
import dog_api as dog
import cat_api as cat

class Sign(MethodView):
    def get(self):
        return render_template('sign.html')
   
    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        species = request.form['species']
        species = species.lower()
        print("species is: \n",species)

        # Based off the species assign either a dog or cat image. 
        if species == "dog":
            rand_image = dog.random_image(request.form['breed'])
        elif species == "cat":
            rand_image = cat.random_image()

        model = gbmodel.get_model()
        model.insert(request.form['name'], request.form['species'], request.form['breed'], request.form['age'], request.form['sex'], request.form['traits'], rand_image)
        return redirect(url_for('index'))



