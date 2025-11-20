CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE
);

CREATE TABLE attendance (
    attendance_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(student_id),
    attendance_date DATE,
    status VARCHAR(15) CHECK (status IN ('Present', 'Absent', 'Leave'))
);

INSERT INTO students (first_name, last_name, email) VALUES ('Test', 'User', 'testuser@email.com');
SELECT * FROM students;
