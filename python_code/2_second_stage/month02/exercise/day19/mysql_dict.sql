# 创建数据库
create database dict charset=utf8;

# 创建数据表
create table words(
id int primary key auto_increment,
word varchar(30) not null,
mean varchar(512) not null
);

create table user(
id int primary key auto_increment,
name varchar(30) not null,
passwords varchar(8) not null
);

create table history(
id int primary key auto_increment,
word varchar(30) not null,
time datetime default now(),
uid int,
constraint user_fk foreign key (uid) references user(id)
);