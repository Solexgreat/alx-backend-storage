-- This sql script creates a new table called users

CREATE TABLE IF NOT EXIST users (
  id INT NOT NULL PRIMARY KEY,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
