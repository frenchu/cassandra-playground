from cassandra.cluster import Cluster
import uuid
import random
import json

locations = ["Gdansk", "Wroclaw", "Poznan", "Lodz", "Krakow", "Warszawa", "Bialystok", "Szczecin", "Olsztyn"]

cluster = Cluster()
session = cluster.connect('shopping')

insert_statement = session.prepare('INSERT INTO purchase_history JSON ?')

for i in range(1_000_000):
    purchase = {
        "shop_location_id": str(uuid.uuid4()),
        "shop_location_city": locations[i % len(locations)],
        "user_id": str(uuid.uuid4()),
        "purchase_time": 1552554900000 + i * 1000 * random.randint(1, 5),
        "purchase": [{
            "product": {
                "name": "Piwniczanka średio nasycona CO2",
                "description": "Naturalna woda mineralna",
                "price": 2.35,
                "categories": ["groceries", "water"]
            },
            "quantity": 2
        }, {
            "product": {
                "name": "Ahmad Earl Grey",
                "description": "Herbata liściasta",
                "price": 6.69,
                "categories": ["groceries", "tea"]
            },
            "quantity": 1
        }]
    }
    session.execute_async(insert_statement, [json.dumps(purchase)])

session.shutdown()
