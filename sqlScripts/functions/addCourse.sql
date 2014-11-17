DELIMITER //
CREATE PROCEDURE addCourse(professor VARCHAR(30), dept VARCHAR(30), courseNo INT,
	sectionNo INT, crn INT, location VARCHAR(30), startHr INT, startMin INT, 
	endHr INT, endMin INT)
BEGIN
	DECLARE event_id INT;

	SELECT addEvent(location, startHr, startMin, endHr, endMin)
	INTO event_id;
	
	INSERT INTO course(crn, professor, dept, courseNo, sectionNo, event_id)
	values(crn, professor, dept, courseNo, sectionNo, event_id); 
END//
DELIMITER ;

