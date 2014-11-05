DELIMITER //
CREATE FUNCTION getPassword(email VARCHAR(30))
RETURNS TEXT
BEGIN
	DECLARE pass VARCHAR(30);

	SELECT password 
	INTO pass
	FROM user 
	WHERE email = email;

	RETURN pass;
END//
DELIMITER ;

