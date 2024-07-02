CREATE table items(
	item_id serial primary key,
	item_name VARCHAR(50) NOT NULL,
	price INTEGER);

CREATE table customers(
	customer_id serial primary key,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR (50) NOT NULL);

insert into items(item_name, price)
values	('small desk', '100'),
		('large desk', '300'),
		('fan', '80');

insert into customers(first_name, last_name)
values	('Greg', 'Jones'),
		('Sandra', 'Jones'),
		('Scot', 'Scot'),
		('Melanie', 'Johnson');


UPDATE customers
SET first_name = 'Scott'
WHERE customer_id = 3;



insert into customers(first_name,last_name)
	VALUES ('Trevor', 'Green');

--Use SQL to fetch the following data from the database:
--All the items.
	
SELECT * FROM items;

-- All the items with a price above 80 (80 not included).

SELECT * FROM items
WHERE price > 80;

-- All the items with a price below 300. (300 included)

SELECT * FROM items
WHERE price <= 300;

-- All customers whose last name is ‘Smith’ (What will be your outcome?).
SELECT * FROM customers
WHERE last_name = 'Smith';


-- All customers whose last name is ‘Jones’.
SELECT * FROM customers
WHERE last_name = 'Jones';


-- All customers whose firstname is not ‘Scott’.

SELECT * FROM customers
WHERE first_name <> 'Scott'; 
--********************************
SELECT * FROM customers
WHERE first_name != 'Scott';



-- update customers
-- set customer_id = 4
-- where customer_id = 15;


-- select * from customers
-- 	ORDER BY customer_id ASC;




