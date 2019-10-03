use eduardo;

CREATE TABLE drink (
	drink_id INTEGER AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100)
);

CREATE TABLE person (
	person_id INTEGER AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100),
	preference INTEGER,
	FOREIGN KEY (preference) REFERENCES drink(drink_id) ON DELETE CASCADE
);

CREATE TABLE rounds (
	round_id INTEGER AUTO_INCREMENT PRIMARY KEY,
	brewer_id INTEGER,
	active BOOLEAN,
	FOREIGN KEY (brewer_id) REFERENCES person(person_id) ON DELETE CASCADE
);

CREATE TABLE orders (
orders_id integer AUTO_INCREMENT PRIMARY KEY,
round_id INTEGER,
person_id INTEGER,
drink_id INTEGER,
FOREIGN KEY (round_id) REFERENCES rounds(round_id) ON DELETE CASCADE,
FOREIGN KEY (person_id) REFERENCES person(person_id) ON DELETE CASCADE,
FOREIGN KEY (drink_id) REFERENCES drink(drink_id) ON DELETE CASCADE
);