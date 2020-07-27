CREATE DATABASE IF NOT EXISTS myinfo;

USE myinfo;

DROP TABLE IF EXISTS AppUser;

CREATE TABLE AppUser (
    user_ID INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(32),
    hashed_password VARCHAR(32),
    password_salt VARCHAR(16),
    first_name VARCHAR(256),
    last_name VARCHAR(256)
) ENGINE = InnoDB;