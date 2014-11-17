DROP TRIGGER IF EXISTS before_course_delete;
DROP TRIGGER IF EXISTS after_course_delete;
\. course_delete.sql

DROP TRIGGER IF EXISTS event_delete;
\. event_delete.sql

DROP TRIGGER IF EXISTS user_delete;
\. user_delete.sql

DROP TRIGGER IF EXISTS note_delete;
\. note_delete.sql

