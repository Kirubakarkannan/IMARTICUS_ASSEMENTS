create database assignment2;
use assignment2;
create table salestable (Product_name varchar(100),price_per_unit int not null,Quantity int not null);
insert into salestable values("Product1",10,28),("Product2",9,30),("Product3",20,28),("Product4",9,28);
select * from salestable;
select Product_name,price_per_unit*Quantity as totalprice from salestable;
