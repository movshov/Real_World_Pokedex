# Real World Pokedex
By: ***Bar Movshovich*** and ***Jordan Le***

***We've got dogs, we've got cats, and we've got facts!***

## How to run:
**http://cs430-bar-movshovich.appspot.com/**

## Assignment Requirements:
Core Functionality (30)
- minimum number of APIs included 
- application builds and runs on GCP
- application handles and processes user input without crashing (API function isn’t hard-coded)
---
Code Content and Organization (40)
- code is clean, readable, and modular
- adapted code is clearly labeled
- personal code contributions evident
- unused files and irrelevant code removed
- descriptive comments present - not everyone is working on the same project for the final so this is a MUST
---
Submission: Code (10)
- git commits are descriptive and document the development process
- repo is updated with the latest final project code
- zipped folder submitted to D2L for a timestamp
---
Screencast Recording (20)
- brief introduction (team members, what is your project/what does it do)
- complete walkthrough of setup steps (from cloning your repo to deploying the app - what would I need to do to run your project on my own machine?)
- walkthrough of the source code and implemented features
- clear mention of individual team members’ contributions  + git history
- demo of application


### Set Up:
* To deploy this flask web application for yourself, you must first create a virtual environment on your google cloud shell with the following commands. Follow the steps listed below in the order in which they appear:
    ```
    virtualenv -p python3 env
    source env/bin/activate
    pip3 install -r requirements.txt
    ```
* Next modify the `self.client` variable in the class `model`'s `__init__` function:
`self.client = datastore.Client('YOUR-GOOGLE-CLOUD-ACCOUNT')`

* For development, run with `python3 app.py` and click the given link to visit the web preview.

* To deploy on google cloud, use the following: `...`

## API's used:
* TheCatAPI - Cats as a Service, Every day is Caturday.
    * https://thecatapi.com/
* Dog CEO - Good Dog Business
    * https://dog.ceo/
* Dog API by kinduff
    * https://kinduff.github.io/dog-api/
* Cat Facts API
    * https://catfact.ninja/

## Real_World_Pokedex/:
| File Name | Description |
| ------ | ------ |
| app.py  | Simple flask app for Real World Pokedex: dogs, cats, and facts. |
| app.yaml | Flask app configuration file for gcloud. |
| index.py | Main page of webapp, renders the template and allows for dynamic html/css. Thank you Jinja. |
| requirements.txt | File which installs the following dependencies: `flask`, `google-cloud-datastore`, `gunicorn`. |
| sign.py | Allows for users to submit a form to google cloud datastore. |

## static/:
| File Name | Description |
| ------ | ------ |
| sytle.css | Technically a style sheet that isn't currently being used, keeps the directory formatting. |

## templates/:
| File Name | Description |
| ------ | ------ |
| index.html | Main html page to greet user. Dynamically adjusted with Jinja. |
| layout.html | Dynamic layout for html and css thanks to Jinja. |

## cat_api/:
| File Name | Description |
| ------ | ------ |
| `__init__.py` | Function initialization for cat api. | 
| utils.py | Defines the `_get` function for the cat api. |
| cat.py | Function definitions for various types of get request to the cat api. |

## cat_fact_api/:
| File Name | Description |
| ------ | ------ |
| `__init__.py` | Function initialization for cat facts api. |
| utils.py | Defines the `_get` function for the cat facts api. |
| cat_fact.py | Function definitions for various types of get request to the cat facts api. |

## dog_api/:
| File Name | Description |
| ------ | ------ |
| `__init__.py` |  Function initialization for dog api.  |
| utils.py | Defines the `_get` function for the dog api. |
| dog_api | Function definitions for various types of get request to the dog api. |

## dog_fact_api/:
| File Name | Description |
| ------ | ------ |
| `__init__.py` |  Function initialization for dog facts api.  |
| utils.py | Defines the `_get` function for the dog facts api. |
| dog_fact.py | Function definitions for various types of get request to the dog facts api. |

## gbmodel/:
| File Name | Description |
| ------ | ------ |
| `__init__.py` | Sets a backend and returns the model. |
| Model.py | Base class for model with a select and insert function. |
| model_datastore.py | Connect to datastore backend. Modify self.client for individual program launch. |


# References:
Transitioning from github to bitbucket:
- https://www.atlassian.com/git/tutorials/git-move-repository

Jinja Template References:
- https://stackoverflow.com/questions/20233721/how-do-you-index-on-a-jinja-template
- https://realpython.com/primer-on-jinja-templating/
- http://www.dataengineering.life/python_vars_in_flask_templates/
- https://stackoverflow.com/questions/12145434/how-to-output-loop-counter-in-python-jinja-template

Css Margins and Layout References:
- https://www.w3schools.com/css/css_margin.asp
- https://www.w3schools.com/css/css_float.asp

APIs:
- https://thecatapi.com/
- https://dog.ceo/
- https://kinduff.github.io/dog-api/
- https://catfact.ninja/

Rain Drop Shape Tutorial:
* https://www.youtube.com/watch?v=CdWPGUkO2nM
