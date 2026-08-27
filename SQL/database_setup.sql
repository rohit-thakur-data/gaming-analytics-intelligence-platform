CREATE DATABASE gaming_analytics_db;

USE gaming_analytics_db;

SHOW TABLES;

SELECT COUNT(*)
FROM player_statistics;

SELECT *
FROM player_statistics
LIMIT 10;

DESCRIBE player_statistics;