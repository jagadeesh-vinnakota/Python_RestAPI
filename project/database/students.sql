drop table IF EXISTS students;
create table students(id int not null primary key, fname varchar(30), lname varchar(30), age int, gender varchar(1));
insert into students values(1,'jaga','vinnakota',25,'M');
insert into students values(2,'mohan','pilla',25,'M');
insert into students values(3,'jagadeesh','vinnakota',25,'M');
select * from students;