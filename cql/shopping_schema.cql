CREATE KEYSPACE shopping WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 3 };

CREATE TYPE shopping.product (
    name text,
    description text,
    price decimal,
    categories set<text>
);

CREATE TYPE shopping.order_item (
    product frozen<product>,
    quantity int
);

CREATE TABLE shopping.purchase_history (
    shop_location_id uuid,
    shop_location_city text,
    user_id uuid,
    purchase_time timestamp,
    purchase frozen<set<order_item>>,
    PRIMARY KEY(shop_location_id, user_id, purchase_time)
);
