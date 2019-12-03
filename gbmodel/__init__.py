"""Decide which model we are going to use"""
#model_backend = 'pylist'
#model_backend = 'sqlite3'
model_backend = 'datastore'

#if we are using sqlite3 use .model_sqlite3's model.
if model_backend == 'sqlite3':
    from .model_sqlite3 import model
#if we are using pylist use .model_pylist's model.
elif model_backend == 'pylist':
    from .model_pylist import model
#if we are using datastore us .model_datastore's model.
elif model_backend == 'datastore':
    from .model_datastore import model
#if we are using neither of these two raise an error.
else:
    raise ValueError("No appropriate databackend configured. ")

appmodel = model()

def get_model():
    return appmodel


