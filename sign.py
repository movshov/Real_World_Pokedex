from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel
import dog_api as dog
import cat_api as cat
import cat_fact_api as cf
import dog_fact_api as df

class Sign(MethodView):
    def get(self):
        return render_template('sign.html')
   
    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """

        try:
            name = request.form['name']
            # check if nothing was inputted.
            if name == '':
                name = None
        except:
            name = None
        try:
            species = request.form['species']
            species = species.lower()
        except:
            species = None
        try:
            breed = request.form['breed']
        except:
            breed = "Unknown"
        try:
            age = request.form['age']
        except:
            age = "Unknown"
        try:
            sex = request.form['sex']
        except:
            sex = "Unknown"
        try:
            traits = request.form['traits']
            # check if nothing was inputted. 
            if traits == '':
                traits = "Unknown"
        except:
            traits = "Unknown"
        


        # Based off the species assign either a dog or cat image. 
        if species == "dog":
            # if the breed is cocker spaniel the breed is spaniel but
            # the subbreed would be cocker. So we split the input to 
            # grab both identifiers.
            rand_fact = df.gimme_dog_fact()
            # Make sure we actually have a breed. 
            if breed is not "Unknown":
                # if we have a subbreed get breed and subbreed.
                if ' ' in breed:
                    subbreed, breed = (request.form['breed'].lower()).split()
                    rand_image = dog.random_image(breed, subbreed)
                # we only have a major breed.
                else:
                    rand_image = dog.random_image(breed)
            # get random image of any dog breed.
            else:
                rand_image = dog.random_image()
            
        # if we have a cat.
        elif species == "cat":
            rand_fact = cf.gimme_cat_fact()
            if breed == "Unknown":
                rand_image = cat.random_image()
            else:
                rand_image = cat.breeds(breed)

        # should never hit. 
        else:
            rand_image = None
            rand_fact = None


        if name is not None and species is not None:
            model = gbmodel.get_model()
            model.insert(name, species, breed, age, sex, traits, rand_image, rand_fact)

        return redirect(url_for('index'))



