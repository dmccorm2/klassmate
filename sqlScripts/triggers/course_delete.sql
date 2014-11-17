DELIMITER //

CREATE TRIGGER after_course_delete AFTER DELETE ON course
FOR EACH ROW
BEGIN
	DELETE FROM event 
	WHERE event_id = OLD.event_id;

	DELETE FROM user_course
        WHERE crn = OLD.crn;

	DELETE FROM note
        WHERE crn = OLD.crn;

END
//

DELIMITER ;	

DELIMITER //

CREATE TRIGGER before_course_delete BEFORE DELETE ON course
FOR EACH ROW
BEGIN
        DELETE FROM user_course
        WHERE crn = OLD.crn;

        DELETE FROM note
        WHERE crn = OLD.crn;

END
//

DELIMITER ;

