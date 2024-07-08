--Bootcamp
--Create a database called bootcamp.
-- Create a table called students.
-- Add the following columns:
-- id
-- last_name
-- first_name
-- birth_date
-- The id must be auto_incremented.
-- Make sure to choose the correct data type for each column.
-- To help, here is the data that you will have to insert. (How do we insert a date to a table?)

--Insert the data seen above to the students table. Find the most efficient way to insert the data.
--Insert your last_name, first_name and birth_date to the students table (Take a look at the id given).
--*****************************************************************************************************

create table students
(
	student_id serial primary key,
	first_name varchar (50) not null,
	last_name varchar (50) not null,
	birth_date date
);

insert into students
	(first_name, last_name, birth_date)
values
	('Marc', 'Benichou', '1998/11/02'),
	('Yoan', 'Cohen', '2010/12/03/'),
	('Lea', 'Benichou', '1987/07/27'),
	('Amelea', 'Dux', '1996/04/07'),
	('David', 'Grez', '2003/06/14'),
	('Omer', 'Simpson', '1980/10/03');

insert into students
	(first_name, last_name, birth_date)
values
	('Meyanui', 'Valentine', '1986/11/11');


-- Select
-- Fetch all of the data from the table.

select *
from students

-- Fetch all of the students first_names and last_names.

select first_name, last_name
from students;

-- For the following questions, only fetch the first_names and last_names of the students.
-- Fetch the student which id is equal to 2.
SELECT *
FROM students
WHERE student_id = 2;


-- Fetch the student whose last_name is Benichou AND first_name is Marc.
SELECT *
FROM students
WHERE last_name = 'Benichou'
	AND first_name = 'Marc';

-- Fetch the students whose last_names are Benichou OR first_names are Marc.
SELECT *
FROM students
WHERE last_name = 'Benichou'
	OR first_name = 'Marc';

-- Fetch the students whose first_names contain the letter a.
SELECT *
FROM students
WHERE first_name LIKE '%a%';
--The LIKE operator is used to match a specified pattern within a string.
--%a%: Matches any string that contains the letter 'a' anywhere in the first_name


-- Fetch the students whose first_names start with the letter a.
SELECT *
FROM students
WHERE first_name
iLIKE 'a%';
-- ilike makes it case insensitive


-- Fetch the students whose first_names end with the letter a.
SELECT *
FROM students
WHERE first_name
iLIKE '%a';


-- Fetch the students whose second to last letter of their first_names are a (Example: Leah).

select first_name, last_name
from students
where (right(first_name, 2) like 'a%')

-- Fetch the students whose id’s are equal to 1 AND 3 .

select first_name, last_name
from students
where (student_id=1 and student_id=3)

-- Fetch the students whose birth_dates are equal to or come after 1/01/2000. (show all their info).
SELECT *
FROM students
WHERE birth_date >= '2000/01/01';


