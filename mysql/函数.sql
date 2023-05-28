delimiter $$
CREATE PROCEDURE customer(
in c_id int,
out c_name varchar(50))
begin
select cust_name from customers where cust_id = c_id into c_name;
end $$
delimiter ;