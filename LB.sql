CREATE DATABASE IF NOT EXISTS LB;
CREATE USER IF NOT EXISTS 'lb'@'localhost' IDENTIFIED BY 'Team_Project';
GRANT ALL PRIVILEGES ON `LB`.* TO 'lb'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'lb'@'localhost';
FLUSH PRIVILEGES;
