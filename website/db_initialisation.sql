CREATE TABLE IF NOT EXISTS administrators (
    id serial PRIMARY KEY,
    first_name VARCHAR (32) NOT NULL,
    last_name VARCHAR (64) NOT NULL,
    email VARCHAR (64) NOT NULL UNIQUE,
    password VARCHAR (64) NOT NULL
);


CREATE TABLE IF NOT EXISTS dormitories (
  id serial PRIMARY KEY,
  number INTEGER UNIQUE NOT NULL,
  address VARCHAR (256) NOT NULL,
  administrator_id INTEGER UNIQUE NOT NULL REFERENCES administrators (id)

);


CREATE TABLE IF NOT EXISTS faculties (
    id SERIAL PRIMARY KEY,
    name VARCHAR (64) NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS residents (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR (32) NOT NULL,
    last_name VARCHAR (64) NOT NULL,
    email VARCHAR (64) NOT NULL UNIQUE,
    room  VARCHAR (32) NOT NULL,
    course INTEGER NOT NULL,
    "group" VARCHAR (32),
    faculty_id INTEGER NOT NULL REFERENCES faculties (id),
    dormitory_id INTEGER NOT NULL REFERENCES dormitories (id)

);

CREATE TABLE IF NOT EXISTS payments (
    id SERIAL PRIMARY KEY,
    time TIMESTAMP DEFAULT now(),
    month_payed INTEGER NOT NULL,
    resident_id INTEGER UNIQUE NOT NULL REFERENCES residents (id)
);

INSERT INTO public.administrators (id, first_name, last_name, email, password)
VALUES (1, 'default', 'default', 'email1@email.com', 'sha256$jyapm1KvL7v2S43S$2a916c8cf7848cbbaca30f8dabae09d84ff51f2b9955cd78112334cf7371e0dd');
INSERT INTO public.administrators (id, first_name, last_name, email, password)
VALUES (3, 'default', 'default', 'email3@email.com', 'sha256$jyapm1KvL7v2S43S$2a916c8cf7848cbbaca30f8dabae09d84ff51f2b9955cd78112334cf7371e0dd');
INSERT INTO public.administrators (id, first_name, last_name, email, password)
VALUES (4, 'default', 'default', 'email4@email.com', 'sha256$jyapm1KvL7v2S43S$2a916c8cf7848cbbaca30f8dabae09d84ff51f2b9955cd78112334cf7371e0dd');
INSERT INTO public.administrators (id, first_name, last_name, email, password)
VALUES (6, 'default', 'default', 'email6@email.com', 'sha256$jyapm1KvL7v2S43S$2a916c8cf7848cbbaca30f8dabae09d84ff51f2b9955cd78112334cf7371e0dd');
INSERT INTO public.administrators (id, first_name, last_name, email, password)
VALUES (7, 'default', 'default', 'email7@email.com', 'sha256$jyapm1KvL7v2S43S$2a916c8cf7848cbbaca30f8dabae09d84ff51f2b9955cd78112334cf7371e0dd');
INSERT INTO public.administrators (id, first_name, last_name, email, password)
VALUES (8, 'default', 'default', 'email8@email.com', 'sha256$jyapm1KvL7v2S43S$2a916c8cf7848cbbaca30f8dabae09d84ff51f2b9955cd78112334cf7371e0dd');
INSERT INTO public.administrators (id, first_name, last_name, email, password)
VALUES (9, 'default', 'default', 'email9@email.com', 'sha256$jyapm1KvL7v2S43S$2a916c8cf7848cbbaca30f8dabae09d84ff51f2b9955cd78112334cf7371e0dd');
INSERT INTO public.administrators (id, first_name, last_name, email, password)
VALUES (10, 'default', 'default', 'email10@email.com', 'sha256$jyapm1KvL7v2S43S$2a916c8cf7848cbbaca30f8dabae09d84ff51f2b9955cd78112334cf7371e0dd');
INSERT INTO public.administrators (id, first_name, last_name, email, password)
VALUES (11, 'default', 'default', 'email11@email.com', 'sha256$jyapm1KvL7v2S43S$2a916c8cf7848cbbaca30f8dabae09d84ff51f2b9955cd78112334cf7371e0dd');
INSERT INTO public.administrators (id, first_name, last_name, email, password)
VALUES (12, 'default', 'default', 'email12@email.com', 'sha256$jyapm1KvL7v2S43S$2a916c8cf7848cbbaca30f8dabae09d84ff51f2b9955cd78112334cf7371e0dd');
INSERT INTO public.administrators (id, first_name, last_name, email, password)
VALUES (13, 'default', 'default', 'email13@email.com', 'sha256$jyapm1KvL7v2S43S$2a916c8cf7848cbbaca30f8dabae09d84ff51f2b9955cd78112334cf7371e0dd');
INSERT INTO public.administrators (id, first_name, last_name, email, password)
VALUES (14, 'default', 'default', 'email14@email.com', 'sha256$jyapm1KvL7v2S43S$2a916c8cf7848cbbaca30f8dabae09d84ff51f2b9955cd78112334cf7371e0dd');
INSERT INTO public.administrators (id, first_name, last_name, email, password)
VALUES (15, 'default', 'default', 'email15@email.com', 'sha256$jyapm1KvL7v2S43S$2a916c8cf7848cbbaca30f8dabae09d84ff51f2b9955cd78112334cf7371e0dd');
INSERT INTO public.administrators (id, first_name, last_name, email, password)
VALUES (16, 'default', 'default', 'email16@email.com', 'sha256$jyapm1KvL7v2S43S$2a916c8cf7848cbbaca30f8dabae09d84ff51f2b9955cd78112334cf7371e0dd');
INSERT INTO public.administrators (id, first_name, last_name, email, password)
VALUES (17, 'default', 'default', 'email17@email.com', 'sha256$jyapm1KvL7v2S43S$2a916c8cf7848cbbaca30f8dabae09d84ff51f2b9955cd78112334cf7371e0dd');
INSERT INTO public.administrators (id, first_name, last_name, email, password)
VALUES (18, 'default', 'default', 'email18@email.com', 'sha256$jyapm1KvL7v2S43S$2a916c8cf7848cbbaca30f8dabae09d84ff51f2b9955cd78112334cf7371e0dd');
INSERT INTO public.administrators (id, first_name, last_name, email, password)
VALUES (19, 'default', 'default', 'email19@email.com', 'sha256$jyapm1KvL7v2S43S$2a916c8cf7848cbbaca30f8dabae09d84ff51f2b9955cd78112334cf7371e0dd');
INSERT INTO public.administrators (id, first_name, last_name, email, password)
VALUES (20, 'default', 'default', 'email20@email.com', 'sha256$jyapm1KvL7v2S43S$2a916c8cf7848cbbaca30f8dabae09d84ff51f2b9955cd78112334cf7371e0dd');
INSERT INTO public.administrators (id, first_name, last_name, email, password)
VALUES (21, 'default', 'default', 'email21@email.com', 'sha256$jyapm1KvL7v2S43S$2a916c8cf7848cbbaca30f8dabae09d84ff51f2b9955cd78112334cf7371e0dd');
INSERT INTO public.administrators (id, first_name, last_name, email, password)
VALUES (22, 'default', 'default', 'email22@email.com', 'sha256$jyapm1KvL7v2S43S$2a916c8cf7848cbbaca30f8dabae09d84ff51f2b9955cd78112334cf7371e0dd');


INSERT INTO public.dormitories (id, number, address, administrator_id)
VALUES (21, 21, 'Kovalskoho lane, 22a', 21);
INSERT INTO public.dormitories (id, number, address, administrator_id)
VALUES (9, 9, 'Academician Yangel street, 16/2 ', 9);
INSERT INTO public.dormitories (id, number, address, administrator_id)
VALUES (6, 6, 'Academician Yangel street, 18/20', 6);
INSERT INTO public.dormitories (id, number, address, administrator_id)
VALUES (19, 19, 'Borschagivska street, 146', 19);
INSERT INTO public.dormitories (id, number, address, administrator_id)
VALUES (10, 10, 'Oleksy Tyhogo street 2/24', 10);
INSERT INTO public.dormitories (id, number, address, administrator_id)
VALUES (1, 1, 'Academician Yangel street, 5', 1);
INSERT INTO public.dormitories (id, number, address, administrator_id)
VALUES (7, 7, 'Metalistiv street, 3', 7);
INSERT INTO public.dormitories (id, number, address, administrator_id)
VALUES (12, 12, 'Metalistiv street, 7/15', 12);
INSERT INTO public.dormitories (id, number, address, administrator_id)
VALUES (16, 16, 'Oleksy Tyhogo street, 3', 16);
INSERT INTO public.dormitories (id, number, address, administrator_id)
VALUES (18, 18, 'Borschagivska street, 148', 18);
INSERT INTO public.dormitories (id, number, address, administrator_id)
VALUES (3, 3, 'Academician Yangel street, 22', 3);
INSERT INTO public.dormitories (id, number, address, administrator_id)
VALUES (4, 4, 'Academician Yangel street, 7', 4);
INSERT INTO public.dormitories (id, number, address, administrator_id)
VALUES (11, 11, 'Metalistiv street, 4', 11);
INSERT INTO public.dormitories (id, number, address, administrator_id)
VALUES (13, 13, 'Metalistiv street, 6/12', 13);
INSERT INTO public.dormitories (id, number, address, administrator_id)
VALUES (22, 22, 'Metalistiv street, 4a', 22);
INSERT INTO public.dormitories (id, number, address, administrator_id)
VALUES (15, 15, 'Metalistiv street, 5', 15);
INSERT INTO public.dormitories (id, number, address, administrator_id)
VALUES (17, 17, 'Oleksy Tyhogo street, 1', 17);
INSERT INTO public.dormitories (id, number, address, administrator_id)
VALUES (14, 14, 'Kovalskoho lane, 5', 14);
INSERT INTO public.dormitories (id, number, address, administrator_id)
VALUES (8, 8, 'Oleksy Tyhogo street, 6/8', 8);
INSERT INTO public.dormitories (id, number, address, administrator_id)
VALUES (20, 20, 'Borschagivska street, 144', 20);


