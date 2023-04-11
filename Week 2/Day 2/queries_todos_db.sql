INSERT INTO users( first_name, last_name, email, password )
VALUES ( 'Julie', 'Winston', 'julie@winston.com', 'pass1234' );

INSERT INTO users( first_name, last_name, email, password )
VALUES ( 'Martha', 'Smith', 'martha@smith.com', 'pass1234' ),
	   ( 'Roger', 'Anderson', 'roger@anderson.com', 'pass1234' ),
       ( 'Julie', 'Winston', 'julie@winston.com', 'pass1234' );

INSERT INTO users( first_name, last_name )
VALUES ( 'Ronald', 'Winston' );

SELECT *
FROM users
WHERE first_name = 'Alex';

SELECT first_name AS 'First name', last_name AS 'Last name'
FROM users;

SELECT *
FROM users
ORDER BY email ASC;

UPDATE users
SET first_name = 'Alexander'
WHERE id = 5;

DELETE FROM users
WHERE id = 4;

INSERT INTO todos( name, status, user_id )
VALUES ( 'Learning Flask', 'complete', 2 ),
       ( 'Learning Sessions', 'complete', 1 ),
       ( 'Learning POST', 'complete', 1 ),
       ( 'Learning SQL', 'in_progress', 2 ),
       ( 'Learning ERD', 'complete', 3 );
  
INSERT INTO todos( name, status, user_id )
VALUES ( 'Integrate SQL with Flask', 'pending', 6 );

SELECT *
FROM todos;

DELETE FROM users
WHERE id = 1;


SELECT *
FROM todos JOIN users
	ON todos.user_id = users.id
WHERE todos.status = 'complete';

SELECT *
FROM todos, users
WHERE todos.user_id = users.id AND todos.status = 'complete';

SELECT t.name, t.status, u.id AS 'User id', UPPER(CONCAT(u.first_name, ' ', u.last_name)) AS 'Full name', RAND()
FROM todos t JOIN users u
	ON t.user_id = u.id
WHERE t.status = 'complete';


SELECT *
FROM users LEFT JOIN todos
	ON todos.user_id = users.id;

SELECT CustomerID, COUNT( CustomerID )
FROM orders
GROUP BY CustomerID;


SELECT *
FROM orders
WHERE CustomerID = 'BERGS';

SELECT *
FROM orders;

SELECT CustomerID, AVG( Freight )
FROM orders
GROUP BY CustomerID
ORDER BY CustomerID DESC;



