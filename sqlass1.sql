create database assignment1;
use database1;
create table HRDATA(nameofemployee varchar(30)not null,empid varchar(20) not null primary key,emp_mob_no int not null,no_of_days_present int not null);
insert into HRDATA values("abc","A123",98754210,28),("cde","C456",87653209,30),("efg","e789",98764200,28),("ghi","G012",98742210,28);
select * from hrdata;




