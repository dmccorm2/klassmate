CREATE TABLE event
(
	event_id int AUTO_INCREMENT,
	location varchar(30),
	startHr int,
	startMin int,
	endHr int,
	endMin int,
	host_id int,
	CONSTRAINT event_pk PRIMARY KEY (event_id),
	CONSTRAINT E_user_fk FOREIGN KEY (host_id) REFERENCES user(user_id) 
);
