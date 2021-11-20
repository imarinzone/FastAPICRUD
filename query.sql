CREATE TABLE if not exists todos (item text);
INSERT INTO todos (item) VALUES ('hello'),('world');

CREATE TABLE customers (
id integer PRIMARY KEY AUTOINCREMENT,
name varcar(200) NOT NULL);

CREATE TABLE Orders (
id integer PRIMARY KEY AUTOINCREMENT,
customer_id integer,
store_id integer,
FOREIGN KEY (store_id) REFERENCES store(id)
FOREIGN KEY (customer_id) REFERENCES customers(id));

CREATE TABLE store (
id integer PRIMARY KEY AUTOINCREMENT,
store_name varcar(200) NOT NULL);

CREATE TABLE tickets (
    id integer PRIMARY KEY AUTOINCREMENT,
    order_id integer,
    amount integer,
    FOREIGN KEY (order_id) REFERENCES Orders(id));