CREATE TABLE event_guest
(
	user_id int,
	event_id int,
	CONSTRAINT EG_pk PRIMARY KEY (user_id, event_id),
	CONSTRAINT EG_event_fk FOREIGN KEY (event_id) REFERENCES event(event_id),
	CONSTRAINT EG_user_fk FOREIGN KEY (user_id) REFERENCES user(user_id) 
);
