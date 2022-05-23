DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS articles;


CREATE TABLE users (
    id      SERIAL PRIMARY KEY NOT NULL,
    name    VARCHAR(200)        NOT NULL,
    email VARCHAR(200)  not null,
    password varchar(200)
);


CREATE TABLE articles (
    id   SERIAL PRIMARY KEY NOT NULL,
    title VARCHAR(40)        NOT NULL,
    writer varchar(30),
    release_date date,
    keywords varchar(40)
);


