DELIMITER //
CREATE PROCEDURE removeUserCourse(IN email VARCHAR(30), IN crn INT)
BEGIN
	DECLARE uid INT;
	SELECT getUserId(email) INTO uid;

	DELETE FROM user_course
	WHERE user_id=uid AND crn=crn;
END//
DELIMITER ;
	

