use eduardo


CREATE TABLE drink (
	drink_id INTEGER AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100)
);


CREATE TABLE person (
	person_id INTEGER AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100),
	preference INTEGER,
	FOREIGN KEY (preference) REFERENCES drink(drink_id)
);


INSERT INTO drink(name) VALUES 
	("Water"), 
	("Black Coffee"), 
	("Americano"), 
	("Latte"), 
	("Cortado"), 
	("Capuccino"), 
	("Tea");