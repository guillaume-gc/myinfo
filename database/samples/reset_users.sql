DROP USER IF EXISTS 'myinfo'@'localhost';
FLUSH PRIVILEGES;

CREATE USER 'myinfo'@'localhost' IDENTIFIED BY 'myinfo';
GRANT ALL PRIVILEGES ON myinfo.* TO 'myinfo'@'localhost' WITH GRANT OPTION;