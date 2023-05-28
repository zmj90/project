create table teacher (
id int primary key auto_increment,
姓名 varchar(9) not null,
编号 varchar(20) not null,
年龄 tinyint unsigned,
职称 varchar(30) not null
);

create table course (
id int primary key auto_increment,
名称 varchar(20),
编号 varchar(20),
学分 tinyint,
tid int,
constraint tid_fk foreign key (tid) references teacher(id)
);

create table student (
id int primary key auto_increment,
姓名 varchar(9),
学号 varchar(20),
年龄 tinyint,
性别 enum('男','女')
);

create table student_course (
id int primary key auto_increment,
score float,
sid int,
cid int,
constraint sid_fk foreign key (sid) references student(id),
constraint cid_fk foreign key (cid) references course(id)
);
