-- script that creates the table unique_id

-- CREATE TABLE , DEFAULT ID  AND UNIQUE
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
