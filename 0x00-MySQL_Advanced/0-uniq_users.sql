-- Check if the table already exists before creating it
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,  -- Auto-incrementing integer primary key
    email VARCHAR(255) NOT NULL UNIQUE,  -- Unique email address, up to 255 characters
    name VARCHAR(255)  -- Name field, up to 255 characters
);
