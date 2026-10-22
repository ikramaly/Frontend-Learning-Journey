create database college;
use college;
create table student(
rollno int primary key,
name varchar (44),
marks int not null ,
grade varchar (1),
city varchar(30)
);

insert into student
(rollno,name,marks,grade,city)
values
(1,"ikram ali",345,"A","delhi"),
(2,"ikram ali",345,"A","mumbai"),
(3,"ikram ali",345,"A","delhi"),
(4,"ikram ali",345,"A","delhi"),
(5,"ikram ali",345,"A","delhi"),
(6,"ikram ali",345,"A","delhi"),
(7,"ikram ali",345,"A","delhi"),
(8,"ikram ali",345,"A","pune");

select * from student;
show tables;

insert into student
(rollno,name, marks,grade,city)
values
(18,"54",34,"F","4785");
select * from student;