use college;
drop table IF EXISTS students;
create table students(id int auto_increment not null primary key, fname varchar(30), lname varchar(30), age int, gender varchar(1));
insert into students(fname,lname,age,gender) values('jaga','vinnakota',25,'M');
insert into students(fname,lname,age,gender) values('mohan','pilla',25,'M');
insert into students(fname,lname,age,gender) values('jagadeesh','vinnakota',25,'M');
select * from students;