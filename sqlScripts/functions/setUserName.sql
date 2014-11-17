DELIMITER //
CREATE PROCEDURE setUserName(IN email VARCHAR(30), IN name VARCHAR(30))
BEGIN
	UPDATE user
	SET name=name
	WHERE email=email;
END//
DELIMITER ;
	

