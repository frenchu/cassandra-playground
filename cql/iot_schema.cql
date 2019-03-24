CREATE KEYSPACE iot WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 2 };

CREATE TYPE iot.measurement (
    temperature float,
    pressure float,
    humidity int,
    caqi int,
    pm25 int,
    pm10 int
);

CREATE TYPE iot.location (
    longitude float,
    latitude float,
    street text,
    city text,
    state text,
    country text,
    tags set<text>
);

CREATE TABLE iot.measurement_result (
    sensor_id uuid,
    sensor_name text,
    sensor_location frozen<location>,
    measurement_time timestamp,
    measurement frozen<measurement>,
    PRIMARY KEY(sensor_id, measurement_time)
);
