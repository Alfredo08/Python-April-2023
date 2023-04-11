CREATE DATABASE todos_db;
USE todos_db;

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `email` varchar(80) NOT NULL,
  `password` varchar(300) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

LOCK TABLES `users` WRITE;
INSERT INTO `users` VALUES (1,'Alex','Miller','alex@miller.com','pass1234','2023-04-11 10:08:30','2023-04-11 10:08:30'),(2,'Martha','Smith','martha@smith.com','pass1234','2023-04-11 10:13:35','2023-04-11 10:13:35'),(3,'Roger','Anderson','roger@anderson.com','pass1234','2023-04-11 10:13:35','2023-04-11 10:13:35'),(5,'Alexander','Winston','alex@winston.com','pass1234','2023-04-11 10:15:23','2023-04-11 10:23:58'),(6,'Julie','Winston','julie@winston.com','pass1234','2023-04-11 10:30:47','2023-04-11 10:30:47');

UNLOCK TABLES;

DROP TABLE IF EXISTS `todos`;
CREATE TABLE `todos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `status` varchar(45) NOT NULL,
  `create_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_todos_users_idx` (`user_id`),
  CONSTRAINT `fk_todos_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
LOCK TABLES `todos` WRITE;

INSERT INTO `todos` VALUES (1,'Learning Flask','complete','2023-04-11 10:34:29','2023-04-11 10:34:29',1),(2,'Learning Flask','complete','2023-04-11 10:35:50','2023-04-11 10:35:50',2),(3,'Learning Sessions','complete','2023-04-11 10:35:50','2023-04-11 10:35:50',1),(4,'Learning POST','complete','2023-04-11 10:35:50','2023-04-11 10:35:50',1),(5,'Learning SQL','in_progress','2023-04-11 10:35:50','2023-04-11 10:35:50',2),(6,'Learning ERD','complete','2023-04-11 10:35:50','2023-04-11 10:35:50',3),(8,'Integrate SQL with Flask','pending','2023-04-11 10:37:56','2023-04-11 10:37:56',6);
UNLOCK TABLES;



