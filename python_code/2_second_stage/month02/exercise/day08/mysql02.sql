练习2: 表关联查询 使用cls 和 interest

1. 学生对应的兴趣爱好以及兴趣班价格
select cls.name,hobby,price
from cls inner join interest on cls.name = interest.name;
2. 查询所有学生信息,同时标注出那些有什么样的兴趣爱好
select cls.%,i.hobby
from cls left join interest as i on cls.name = i.name;
3. 查询所有兴趣班信息,同时标注有那些学生参加了这些兴趣班
select i.*,cls.name
from cls right join interest as i on i.name = cls.name;