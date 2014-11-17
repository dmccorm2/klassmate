#returns id
DELIMITER //
CREATE FUNCTION addUser(email VARCHAR(30), password VARCHAR(30))
RETURNS INT
BEGIN
	DECLARE ret INT;

	INSERT INTO user(email, password)
	VALUES (email, password);
	
	SELECT getUserId(email)
 	INTO ret;

	RETURN ret;

END//
DELIMITER ;
	

