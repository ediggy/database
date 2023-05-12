
drop table if exists games;
drop table if exists posts;

create table posts(
    id integer primary key autoincrement,
    title text not null,
    genre text default null,
    content text not null,
    developer text default null,
    price float default null,
    test integer not null
);

drop table if exists test1;

create table test1(
    id integer primary key autoincrement,
    title text not null,
    content text not null
);

drop table if exists test2;

create table test2(
    id integer primary key autoincrement,
    title text not null,
    content text not null
);

drop table if exists test3;

create table test3(
    id integer primary key autoincrement,
    title text not null,
    content text not null
);

drop table if exists final;

create table final(
    id integer primary key autoincrement,
    title text not null,
    content text not null
);