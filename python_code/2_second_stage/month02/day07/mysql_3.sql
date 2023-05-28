-- 练习1 : 使用book表完成
-- 1. 统计每位作家图书的平均价格
select author,avg(price) from book group by author;

-- 2. 统计每个出版社出版图书的数量
select publication,count(*) from book group by publication;

-- 3. 查看总共有多少个出版社
select count(distinct publication) from book;


-- 4. 筛选出那些出版过超过50元图书的出版社,并且按照其最高价格图书倒叙排序
 select publication,max(price)
 from book
 group by publication
 having max(price) > 50
 order by max(price) desc;

-- 5. 统计相同出版时间的图书的平均价格
select publication_time,avg(price) from book group by publication_time;

-- 外键关系
insert into dept values
(1,"技术部"),
(2,"财务部"),
(3,"销售部"),
(4,"行政部"),
(5,"市场部");

insert into person values
(1,"Lily",29,'w',20000,'2017-4-3',2),
(2,"Tom",27,'m',16000,'2019-10-3',1),
(3,"Joy",30,'m',28000,'2016-4-3',1),
(4,"Emma",24,'w',8000,'2019-5-8',4),
(5,"Abby",28,'w',17000,'2018-11-3',3),
(6,"Jame",32,'m',22000,'2017-4-7',3);

级联动作
alter table person add constraint dept_fk foreign key(dept_id) references dept(id) on delete cascade on update cascade;
alter table person add constraint dept_fk foreign key(dept_id) references dept(id) on delete set null on update set null;


作业:
    1. 语句熟练一遍

    2. 设计朋友圈,用户,点赞评论数据的存储
    建立相应的表模型

    提示: 多对多关系可能衍生数据

