-- Delete all tables within the database
USE LB;
SET FOREIGN_KEY_CHECKS = 0; -- Disable foreign key checks temporarily

-- Gather all table names
SET @tables = NULL;
SELECT GROUP_CONCAT(table_name) INTO @tables
  FROM information_schema.tables
  WHERE table_schema = 'LB';

-- Drop all tables
SET @tables = CONCAT('DROP TABLE IF EXISTS ', @tables);
PREPARE stmt FROM @tables;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET FOREIGN_KEY_CHECKS = 1; -- Enable foreign key checks again

-- Drop the database itself
DROP DATABASE IF EXISTS LB;
