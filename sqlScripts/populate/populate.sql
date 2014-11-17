#id 0
INSERT INTO user(name, email, professor, password)
values( 'Zach Lipp', 'zlipp@nd.edu', 0, 'SoftEg');

#event 0
INSERT INTO event(location, startHr, startMin, endHr, endMin)
values('125 Debartolo', 9, 25, 10, 15);

#
INSERT INTO course(professor, dept, courseNo, sectionNo, crn, event_id)
values('McMillan', 'CSE', 40232, 1, 15947, 1);

INSERT INTO event_day(event_id, day)
values(1, 1);

INSERT INTO event_day(event_id, day)
values(1, 3);

INSERT INTO event_day(event_id, day)
values(1, 5);

INSERT INTO event_guest(user_id, event_id)
values(4, 1);

