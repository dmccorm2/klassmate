CREATE TABLE user_course
(
	user_id int,
	crn int,
	CONSTRAINT UC_pk PRIMARY KEY (user_id, crn),
	CONSTRAINT UC_crn_fk FOREIGN KEY (crn) REFERENCES course(crn),
	CONSTRAINT UC_user_fk FOREIGN KEY (user_id) REFERENCES user(user_id) 
);
