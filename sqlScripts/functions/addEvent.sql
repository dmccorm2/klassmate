#host_id can be null
DELIMITER //
CREATE FUNCTION addEvent(location VARCHAR(30), startHr INT,
	startMin INT, endHr INT, endMin INT, host_id INT)
RETURNS INT
BEGIN
	DECLARE ret INT;

	INSERT INTO event(location, startHr, startMin, endHr, endMin, host_id)
	values(location, startHr, startMin, endHr, endMin, host_id);
	
	SELECT MAX(event_id)
	INTO ret
	FROM event; 

	RETURN ret;
END//
DELIMITER ;

