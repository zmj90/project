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

insert into class(caption) values
('三年二班'),('三年三班'),('三年一班');
insert into teacher(tname) values
('波多老师'),('苍老师'),('小泽老师');
insert into student(sname,gender,class_id) values
('钢蛋','female',1),('铁锤','female',1),('山炮','male',2),('彪哥','male',3);
insert into course(cname,teacher_id) values
('生物',1),('体育',1),('物理',2);
insert into score(student_id,course_id,number) values
(1,1,60),(1,2,59),(2,2,100),(3,2,78),(4,3,66);

1. 查询每位老师教授的课程数量
select tname as 名字,count(cname) as 课程数量
from teacher left join course on tid = teacher_id
group by 名字 order by 名字 desc;
2. 查询学生的信息及学生所在班级信息
select sname as 姓名,gender as 性别,caption as 班级
from student left join class on class_id = cid;
3. 查询各科成绩最高和最低的分数,形式 : 课程ID  最高分  最低分
select course_id as 课程ID,max(number) as 最高分,min(number) as 最低分
from score group by 课程ID order by 课程ID;
4. 查询平均成绩大于85分的所有学生学号,姓名和平均成绩
select student.sid as 学号,sname as 姓名,avg(number) as 平均成绩
from student left join score on student.sid = student_id
group by 学号 having avg(number) > 85;
5. 查询课程编号为2且课程成绩在80以上的学生学号和姓名
select student.sid as 学号,sname as 姓名,course_id as 课程编号,number as 成绩
from student right join
(select * from score where course_id = 2 and number > 80) as sc
on student.sid = student_id;
6. 查询各个课程及相应的选修人数
select cname as 课程,count(course_id) as 人数
from course left join score on cid = course_id
group by 课程 order by 课程;