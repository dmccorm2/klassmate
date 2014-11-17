DELIMITER //

CREATE TRIGGER event_delete BEFORE DELETE ON event
FOR EACH ROW
BEGIN
	DELETE FROM event_day 
	WHERE event_id = OLD.event_id;

	DELETE FROM event_guest
        WHERE event_id = OLD.event_id;

END
//

DELIMITER ;	
