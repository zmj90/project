-- 朋友圈设计练习

-- 用户
create table user(
id int primary key auto_increment,
name varchar(30),
passwd char(64)
);

-- 朋友圈内容
create table pyq(
id int primary key auto_increment,
content text,
image blob,
time datetime,
u_id int,
constraint u_fk foreign key (u_id) references user(id)
);

-- 点赞评论
create table user_pyq(
id int primary  key auto_increment,
uid int,
pid int,
lk bit default 0,
comment text,
constraint ufk foreign key (uid) references user(id),
constraint pfk foreign key (pid) references pyq(id)
);


-- 练习: 对应笔记中ER模型图,建立教师,学生,课程三个实体之间的表关系

create table teacher(
id int primary key  auto_increment,
姓名 varchar(30),
职称 varchar(50),
年龄 tinyint
);

create table stu(
id int primary key  auto_increment,
姓名 varchar(30),
年龄 tinyint,
性别 char,
籍贯 varchar(128)
);

create table course(
id int primary key  auto_increment,
名称 varchar(30),
学分 float,
tid int,
constraint t_fk
foreign key (tid)
references teacher(id)
);

create table course_stu(
cid int,
sid int,
score float,
constraint c_fk
foreign key (cid)
references course(id),
constraint s_fk
foreign key (sid)
references stu(id)
);


-- 多表查询
查询技术部工资高于20000的
select * from
(select d.dname,p.name,p.salary
from dept as d,person as p
where d.id = p.dept_id) as a
where dname='技术部' and salary > 20000;

select dept.dname,person.name,person.salary
from dept inner join person on dept.id=person.dept_id
where dname='技术部' and salary > 20000;

-- 部门ID大于1的所有部门及人员
select dept.dname,person.name
from dept left join person on dept.id = person.dept_id
where dept.id > 1;

-- 工资高于20000的人员和部门
select person.name,dept.dname
from dept right join person on dept.id = person.dept_id
where person.salary>=20000;

练习2: 表关联查询 使用cls 和 interest

     1. 学生对应的兴趣爱好以及兴趣班价格
     select cls.name,interest.hobby,interest.price
     from cls inner join interest on cls.name=interest.name;

     2. 查询所有学生信息,同时标注哪些同学有什么样的兴趣爱好
    select c.name,c.sex,i.hobby
    from cls as c left join interest as i on c.name=i.name;

     3. 查询所有兴趣班信息,同时标注有那些学生参加了这些兴趣班
     select i.hobby,i.price,c.name
     from cls as c right join interest as i on c.name=i.name;


进阶练习:

create table class(cid int primary key auto_increment,
                  caption char(4) not null);

create table teacher(tid int primary key auto_increment,
                    tname varchar(32) not null);

create table student(sid int primary key auto_increment,
                    sname varchar(32) not null,
                    gender enum('male','female','others') not null default 'male',
                    class_id int,
                    foreign key(class_id) references class(cid)
                    on update cascade
                    on delete cascade);

create table course(cid int primary key auto_increment,
                   cname varchar(16) not null,
                   teacher_id int,
                   foreign key(teacher_id) references teacher(tid)
                   on update cascade
                   on delete cascade);

create table score(sid int primary key auto_increment,
                  student_id int,
                  course_id int,
                  number int(3) not null,
                  foreign key(student_id) references student(sid)
                   on update cascade
                   on delete cascade,
                   foreign key(course_id) references course(cid)
                   on update cascade
                   on delete cascade);

insert into class(caption) values('三年二班'),('三年三班'),('三年一班');
insert into teacher(tname) values('波多老师'),('苍老师'),('小泽老师');
insert into student(sname,gender,class_id) values('钢蛋','female',1),('铁锤','female',1),('山炮','male',2),('彪哥','male',3);
insert into course(cname,teacher_id) values('生物',1),('体育',1),('物理',2);
insert into score(student_id,course_id,number) values(1,1,60),(1,2,59),(2,2,100),(3,2,78),(4,3,66);

1. 查询每位老师教授的课程数量
2. 查询学生的信息及学生所在班级信息
3. 查询各科成绩最高和最低的分数,形式 : 课程ID  最高分  最低分
4. 查询平均成绩大于85分的所有学生学号,姓名和平均成绩
5. 查询课程变化为2且课程成绩在80以上的学生学号和姓名
6. 查询各个课程及相应的选修人数


-- 视图操作
create view person_dept as (select p.id,p.name,p.age,p.sex,p.salary,d.dname from person as p left join dept as d on p.dept_id = d.id);

替换视图
create or replace  view p1 as select * from person where age>28;


函数使用

错误示例1 : 函数中不能有查询操作
create function st1() returns int
begin
select * from cls;
return (select score from cls limit 1);
end $$

示例2 函数中可以有写操作,每次调用函数都会执行 (是否真的每次调用都执行这种写操作)
create function st1() returns int
begin
insert into cls (name,age,sex,score) values ('Jame',16,'m',88);
update cls set score=99 where id=1;
return (select score from cls limit 1);
end $$

# 使用变量获取值
create function st2()
returns int
begin
declare val1 float;
declare val2 float;
set val1=(select score from cls order by score desc limit 1);
select score from cls order by score limit 1 into val2;
return val1+val2;
end $$

# 带有参数的函数
create function queryNameById(uid int)
returns varchar(20)
begin
return  (select name from cls where id=uid);
end $$
delimiter ;


存储过程
in 类型形参
create procedure p_in ( in num int )
begin
    select num;
    set num=100;
    select num;
end $$




out类型变量
create procedure p_out ( OUT num int )
begin
    select num;
    set num=100;
    select num;
end $$


函数存储过程操作

查看函数信息
show function status like "st1";

查看存储过程内容
show create procedure st;

查看数据库中的存储过程
select name from mysql.proc where db='stu' and type='procedure';

删除
drop function queryNameById;
