CREATE TABLE course
(
	crn int,
	professor varchar(30),
	dept varchar(30),
	courseNo varchar(30),
	sectionNo varchar(30),
	event_id int,
	CONSTRAINT course_pk PRIMARY KEY (crn)
);
