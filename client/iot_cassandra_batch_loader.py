from cassandra.cluster import Cluster
import uuid
import random
import json
import string

cluster = Cluster()
session = cluster.connect('iot')

insert_statement = session.prepare('INSERT INTO purchase_history JSON ?')

for i in range(10_000_000):
    measurement = {
        "sensor_id": str(uuid.uuid4()),
        "sensor_name": ''.join(random.choice(string.ascii_lowercase) for _ in range(10)),
        "sensor_location": {
            "longitude": 40.4240,
            "latitude": 86.9290
        },
        "measurement_time": 1520982000000 + i * 1000,
        "measurement": {
            "temperature": 10.5,
            "pressure": 1015.2,
            "humidity": 41,
            "caqi": random.randint(50, 150),
            "pm25": random.randint(10, 50),
            "pm10": random.randint(20, 100)
        }
    }
    session.execute_async(insert_statement, [json.dumps(measurement)])

session.shutdown()
