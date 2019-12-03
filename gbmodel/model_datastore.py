# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .Model import Model
from datetime import datetime
from google.cloud import datastore

def from_datastore(entity):
    """Translates Datastore results into the format expected by the
    application.

    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]

    This returns:
        [ name, email, date, message ]
    where name, email, and message are Python strings
    and where date is a Python datetime
    """
    if not entity:
        return None
    if isinstance(entity, list):
        entity = entity.pop()
    return [entity['name'],entity['street_address'],entity['city'],entity['state'],entity['zip_code'],entity['store_hours'],entity['phone_number'],entity['rating'],entity['review'],entity['drink_order']]

class model(Model):
    def __init__(self):
        self.client = datastore.Client('cs430-bar-movshovich')

    def select(self):
        query = self.client.query(kind = 'Bobba_Entry')
        entities = list(map(from_datastore,query.fetch()))
        return entities

    def insert(self, name, street_address, city, state, zip_code, store_hours, phone_number, rating, review, drink_order):
        key = self.client.key('Bobba_Entry')
        rev = datastore.Entity(key)
        rev.update( {
            'name': name,
	    'street_address': street_address,
	    'city': city,
	    'state': state,
	    'zip_code': zip_code,
	    'store_hours': store_hours,
	    'phone_number': phone_number,
	    'rating': rating,
            'review': review,
            'drink_order': drink_order
            })
        self.client.put(rev)
        return True

