DELIMITER //
CREATE PROCEDURE setUserPassword(IN email VARCHAR(30), IN pass VARCHAR(30))
BEGIN
	UPDATE user
	SET password=pass
	WHERE email=email;
END//
DELIMITER ;
	

