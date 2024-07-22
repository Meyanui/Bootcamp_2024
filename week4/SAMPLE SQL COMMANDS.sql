--SAMPLE SQL COMMANDS

-- Create a table
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    grade VARCHAR(10),
    email VARCHAR(100)
);

-- Insert data into the table
INSERT INTO students (name, age, grade, email)
VALUES ('Alice Smith', 14, '9th Grade', 'alice@example.com'),
       ('Bob Johnson', 15, '10th Grade', 'bob@example.com');

-- Query the table
SELECT * FROM students;

-- Update data in the table
UPDATE students
SET age = 16
WHERE name = 'Bob Johnson';

-- Delete data from the table
DELETE FROM students
WHERE name = 'Alice Smith';

-- Alter the table to add a new column
ALTER TABLE students
ADD COLUMN phone_number VARCHAR(15);

-- Drop the table
DROP TABLE students;
