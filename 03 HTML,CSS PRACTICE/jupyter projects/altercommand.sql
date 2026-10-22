CREATE DATABASE college_db;
DROP DATABASE college_db;
USE college_db;
CREATE TABLE dep(
id INT PRIMARY KEY ,
name VARCHAR(40)
);
INSERT INTO dep
(id,name)
VALUES
(101,'HINDI'),
(102,'ENGLISH'),
(103,'MATH'),
(104,'PHYSICS'),
(106,'HINDI'),
(107,'ENGLISH'),
(108,'MATH'),
(109,'PHYSICS');



ALTER TABLE dep
ADD COLUMN fee INT ;

ALTER table dep
DROP COLUMN name ;

ALTER TABLE DEP
RENAME to dep1;

ALTER TABLE dep1
modify fee varchar(50) ;

ALTER TABLE dep1 
CHANGE COLUMN id ido varchar(89);
SELECT * FROM dep1;

update table dep1