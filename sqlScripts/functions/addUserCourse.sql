DELIMITER //
CREATE PROCEDURE addUserCourse(IN email VARCHAR(30), IN crn INT)
BEGIN
	DECLARE uid INT;
	SELECT getUserId(email) INTO uid;

	INSERT INTO user_course(user_id, crn)
	VALUES(uid,crn);
END//
DELIMITER ;
	

