create database assignment5;
use assignment5;
create table table2(Division_id int,Year_ int,revenue int);
insert into table2 values(1,2018,60),(1,2021,40),(1,2020,70),(2,2021,-10),(3,2018,20),(3,2016,40),(4,2021,50);
select * from table2 where revenue>=1 and year_=2021;
