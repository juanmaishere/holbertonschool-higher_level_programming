-- Display a fulll table :D

-- Get table structure information without using DESCRIBE or EXPLAIN
SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'first_table';
