create database ikramdb;
use ikramdb;
create table students(
id int primary key ,
name varchar(45),
age int not null
);
insert into students
(id,name,age)
values
(20,"ikram ali",45),
(21,"khushi sanghal",46),
(22,"manish kumar ",47),
(23,"shahid ali",43),
(24,"abrar khan",24),
(25,"virat kohli",94),
(26,"tanu panwar",14);

select * from students limit 3;
select * from students where age>54 and name="tanu" limit 300;
select * from students order by name asc;
select * from students order by age desc;
