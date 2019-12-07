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
        species = request.form['species']
        species = species.lower()
        print("species is: \n",species)

        # Based off the species assign either a dog or cat image. 
        if species == "dog":
            # if the breed is cocker spaniel the breed is spaniel but
            # the subbreed would be cocker. So we split the input to 
            # grab both identifiers.
            subbreed = None
            breed = None
            rand_fact = df.gimme_dog_fact()
            input1 = request.form['breed']
            print("input1 is: \n", input1)
            if ' ' in input1:
                print("space was true")
                subbreed, breed = (request.form['breed'].lower()).split()
                print("breed is: \n", breed)
                print("subbreed is: \n", subbreed)
                rand_image = dog.random_image(breed, subbreed)
            else:
                rand_image = dog.random_image(input1)
            
        elif species == "cat":
            rand_image = cat.random_image()
            rand_fact = cf.gimme_cat_fact()
        else:
            rand_image = None
            rand_fact = None

        model = gbmodel.get_model()
        model.insert(request.form['name'], request.form['species'], request.form['breed'], request.form['age'], request.form['sex'], request.form['traits'], rand_image, rand_fact)
        return redirect(url_for('index'))



