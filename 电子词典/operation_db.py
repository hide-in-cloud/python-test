"""

* 用户 class user --> (id, name, passwd)
create table user(
    id int primary key auto_increment,
    name varchar(32) not null,
    passwd varchar(128) not null
    );

* 历史记录 history --> (id, name, word, time)
create table history(
    id int primary key auto_increment,
    name varchar(32) not null,
    word varchar(28) not null,
    time datetime default now()
    );

"""


