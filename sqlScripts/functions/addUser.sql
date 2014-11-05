DELIMITER //
CREATE PROCEDURE addUser(IN email VARCHAR(30), IN password VARCHAR(30))
BEGIN
	INSERT INTO user(email, password)
	VALUES (email, password);
END//
DELIMITER ;
	

