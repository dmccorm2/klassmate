CREATE TABLE note_keyword
(
	note_id int,
	keyword varchar(30),
	CONSTRAINT NK_pk PRIMARY KEY (note_id, keyword),
	CONSTRAINT NK_note_fk FOREIGN KEY (note_id) REFERENCES note(note_id) 
);
