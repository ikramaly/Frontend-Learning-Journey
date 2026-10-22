create database ikram ;
use ikram;
create table ali(
id int primary key ,
name varchar(50),
age int not null
);

insert into ali 
(id,name,age)
values
(11,"ikram ali",44),
(34,"ali",34);

select * from ali;
select id,name from ali;
select age from ali;

show tables;
select * from ali where age>73;
select * from ali where age>73 and name="ikram";
select * from ali where age>3 and id > -4;
