DELIMITER //
CREATE PROCEDURE setUserProfessor(IN email VARCHAR(30), IN prof BOOL)
BEGIN
	UPDATE user
	SET professor=prof
	WHERE email=email;
END//
DELIMITER ;
	

