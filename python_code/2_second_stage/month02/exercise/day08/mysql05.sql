-- 2. 函数 传入两个学生的ID 得到这两个学生的成绩之和
--    存储过程  传入一个学生的姓名 通过外部的用户变量得到这个学生的成绩
delimiter //
create function get_sum_score1 (id1 int,id2 int)
returns float
begin
declare score1 float;
declare score2 float;
select score from cls where id = id1 into score1;
select score from cls where id = id2 into score2;
return score1 + score2;
end //
delimiter ;
select get_sum_score1 (1,2);

delimiter //
create procedure get_score(in uname varchar(30))
begin
set @score=(select score from cls where name=uname);
end //
delimiter ;

call get_score('Lily');
select @score;