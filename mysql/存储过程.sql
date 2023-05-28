delimiter $$
create procedure test.in_param(in p_in int)
begin
select p_in;
set p_in=2;
select p_in;
end$$
delimiter ;

delimiter $$
create procedure io_param(in p_in int, out date_time datetime)
begin
select p_in;
set p_in=2;
select p_in;
set date_time=now();
end$$
delimiter ;

delimiter $$
create procedure inout_param(inout p_in int)
begin
select p_in;
set p_in=2;
select p_in;
end$$
delimiter ;

delimiter $$
create procedure fun1(in c int)
begin
declare a int default 1;
declare b int default 2;
if c=a+b then
select c;
end if;
if c!=a+b then
select a, b;
else
select c;
end if;
end $$
delimiter ;