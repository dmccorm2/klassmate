DELIMITER //

CREATE TRIGGER user_delete BEFORE DELETE ON user
FOR EACH ROW
BEGIN
	DELETE FROM event_guest
        WHERE user_id = OLD.user_id;

	DELETE FROM user_course
        WHERE user_id = OLD.user_id;

        DELETE FROM event
        WHERE host_id = OLD.user_id;

        UPDATE notes
        SET author_id = NULL
	WHERE author_id = OLD.user_id;

END
//

DELIMITER ;

