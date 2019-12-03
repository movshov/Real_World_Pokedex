"""Specify that we are using the datastore model"""
model_backend = 'datastore'
from .model_datastore import model

appmodel = model()

def get_model():
    return appmodel


