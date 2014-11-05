DROP TABLE IF EXISTS event_guest;
DROP TABLE IF EXISTS event_day;
DROP TABLE IF EXISTS user_course;
DROP TABLE IF EXISTS note_keyword;
DROP TABLE IF EXISTS note;
DROP TABLE IF EXISTS course;
DROP TABLE IF EXISTS event;
DROP TABLE IF EXISTS user;

\. user.sql
\. event.sql
\. course.sql
\. note.sql
\. user_course.sql
\. note_keyword.sql
\. event_day.sql
\. event_guest.sql
