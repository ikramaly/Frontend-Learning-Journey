CREATE DATABASE ikram_db;
USE ikram_db;
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
(104,'PHYSICS');

CREATE TABLE teacher(
id INT PRIMARY KEY ,
name VARCHAR(55),
marks int
);
INSERT INTO teacher
(id,name,marks)
VALUES
(101,'IKRAM ALI',101),
(102,'RANA G',102),
(103,'MANISH KUMAR',103),
(104,'KAZMI',102),
(105,'IKRRAM ALI',104),
(106,'RAHIL RAJ',101),
(107,'SOUNU NIGAM',104);

SELECT *
FROM dep
FULL join teacher
on dep.id=teacher.id;