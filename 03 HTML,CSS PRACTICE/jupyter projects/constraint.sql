create database constraints;
use constraints;
create table students(
id int primary key,
age int check (age >=18),
city varchar(47) check (city="delhi")



);


insert into students value (376,3,"delhi");
insert into students value (34,28,"delhi");
insert into students value (45,47,"pine");
select * from students;
