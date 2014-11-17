#user functions
#-------------------------------------------
DROP FUNCTION IF EXISTS addUser;
\. addUser.sql

DROP PROCEDURE IF EXISTS setUserName;
\. setUserName.sql

DROP PROCEDURE IF EXISTS setUserPassword;
\. setUserPassword.sql

DROP PROCEDURE IF EXISTS setUserEmail;
\. setUserEmail.sql

DROP PROCEDURE IF EXISTS setUserProfessor;
\. setUserProfessor.sql

DROP FUNCTION IF EXISTS getPassword;
\. getPassword.sql

DROP FUNCTION IF EXISTS getUserName;
\. getUserName.sql

DROP FUNCTION IF EXISTS getUserId;
\. getUserId.sql




#user_course functions
#---------------------------------------------
DROP PROCEDURE IF EXISTS addUserCourse;
\. addUserCourse.sql

DROP PROCEDURE IF EXISTS removeUserCourse;
\. removeUserCourse.sql




#event
#----------------------------------------------
DROP FUNCTION IF EXISTS addEvent;
\. addEvent.sql


#class
#------------------------------------------------
DROP PROCEDURE IF EXISTS addCourse;
\. addCourse.sql



DROP PROCEDURE IF EXISTS addCourseDay;
\. addCourseDay.sql

