CREATE DATABASE IF NOT EXISTS LB;
CREATE USER IF NOT EXISTS 'lb'@'localhost' IDENTIFIED BY 'Team_Project';
GRANT ALL PRIVILEGES ON `LB`.* TO 'lb'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'lb'@'localhost';
FLUSH PRIVILEGES;

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
    parent_id
) VALUES (
    'John', 
    'M.', 
    'Doe', 
    'john.doe@example.com',
    'john.doe@example.com', 
    'hashed_password',  -- Ensure to hash the password before inserting
    '2005-05-15', 
    19, 
    'path/to/image.jpg', 
    'Male', 
    '123 Main St', 
    '123-456-7890', 
    '10', 
    'A', 
    NULL,  -- Assuming admin_id is not provided
    NULL   -- Assuming parent_id is not provided
);

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
    created_at
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
    NOW()
);