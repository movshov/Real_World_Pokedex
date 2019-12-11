eal World Pokedex
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
| static/ | |

## templates/:
| File Name | Description |
| ------ | ------ |
| templates/ | |

## cat_api/:
| File Name | Description |
| ------ | ------ |
| `__init__.py` |  | 
| utils.py | |
| cat.py | |

## cat_fact_api/:
| File Name | Description |
| ------ | ------ |
| `__init__.py` | |
| utils.py | |
| cat_fact.py | |

## dog_api/:
| File Name | Description |
| ------ | ------ |
| `__init__.py` | |
| utils.py | |
| dog_api | |

## dog_fact_api/:
| File Name | Description |
| ------ | ------ |
| `__init__.py` | |
| utils.py | |
| dog_fact.py | |

## gbmodel/:
| File Name | Description |
| ------ | ------ |
| `__init__.py` | |
| Model.py | |
| model_datastore.py | |
