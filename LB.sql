CREATE DATABASE IF NOT EXISTS LB;
CREATE USER IF NOT EXISTS 'lb'@'localhost' IDENTIFIED BY 'Team_Project';
GRANT ALL PRIVILEGES ON `LB`.* TO 'lb'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'lb'@'localhost';
FLUSH PRIVILEGES;

USE LB;
-- to insert new student data.
INSERT INTO students (
    firstname,
    middlename,
    lastname,
    email,
    password,
    birth_date,
    age,
    image_file,
    gender,
    address,
    phone_no,
    grade,
    section,
    admin_id,
    parent_id,
    created_at,
    id,
    updated_at
) VALUES (
    'John',
    'M.',
    'Doe',
    'john.doe@example.com',
    'hashed_password',
    '2005-05-15',
    19,
    'default', 
    'Male',
    '123 Main St',
    '123-456-7890',
    '10',
    'A',
    NULL,
    NULL,
    NOW(),
    '123abc',
    NOW()
);

-- # proxy_pass http://unix:/root/LB_backup/learningbridge.sock;