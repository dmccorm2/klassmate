CREATE TABLE user
(
	user_id INT AUTO_INCREMENT,
	name varchar(30),
	email varchar(30) UNIQUE,
	password varchar(30),
	professor BOOL,
	CONSTRAINT user_pk PRIMARY KEY (user_id)
);
