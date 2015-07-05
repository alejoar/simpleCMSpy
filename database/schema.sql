-- Schema for to-do application examples.

-- Users table. Passwords will be just hashed for now..
create table users (
    name        text primary key,
    password    integer
);

-- News table
create table news (
    id           integer primary key autoincrement not null,
    title        text,
    content      text,
    date         date,
    author       text not null references users(name)
);