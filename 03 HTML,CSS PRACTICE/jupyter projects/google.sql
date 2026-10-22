create database university;
use university;
create table students(
id int ,
name varchar(56),
age int not null,
fee int default 67000,
primary key(id , name )
);


insert into students value(2,"ikram ali",45,4383);
insert into students value(20,"ikram ali",45,43983);
insert into students (id , name ,age) value(3,"ikram",45);
insert into students (id , name , age )value(3,"ikram ali",45);

select * from students;

insert into students
(id,name,age,fee)
values
(23,"ikram ali",57,38477),
(34,"manish kumar",92,90000);

select * from students;

create database if not exists youtube;
use youtube;
create table videos(
id int primary key,
name varchar(50) default "ikram ali"
);
insert into videos value(23,"ikram aki");
insert into videos (id) value(34);

select * from videos;
