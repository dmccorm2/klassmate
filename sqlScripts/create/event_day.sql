CREATE TABLE event_day
(
	event_id int,
	day int,
	CONSTRAINT ED_pk PRIMARY KEY (event_id, day),
	CONSTRAINT ED_event_fk FOREIGN KEY (event_id) REFERENCES event(event_id) 
);
