DELIMITER //
CREATE PROCEDURE setUserEmail(IN oldEmail VARCHAR(30), IN newEmail VARCHAR(30))
BEGIN
	UPDATE user
	SET email=newEmail
	WHERE email=email;
END//
DELIMITER ;
	

