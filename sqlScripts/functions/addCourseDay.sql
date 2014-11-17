DELIMITER //
CREATE PROCEDURE addCourseDay(crn INT, day INT)
BEGIN
	DECLARE event_id INT;

	SELECT event_id
	INTO event_id
	FROM course
	WHERE crn = crn;
	
	INSERT INTO event_day(event_id, day)
	values(event_id, day); 
END//
DELIMITER ;

