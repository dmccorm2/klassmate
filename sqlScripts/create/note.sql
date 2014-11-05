CREATE TABLE note
(
	crn int,
	filename varchar(30),
	title varchar(30),
	author_id int,
	note_id int AUTO_INCREMENT,
	CONSTRAINT note_pk PRIMARY KEY (note_id),
	CONSTRAINT N_crn_fk FOREIGN KEY (crn) REFERENCES course(crn),
	CONSTRAINT N_user_fk FOREIGN KEY (author_id) REFERENCES user(user_id) 
);
