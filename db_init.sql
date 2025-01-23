create table if not exists users (
    user_id bigserial primary key,
    encrypted_token varchar unique not null,
    is_admin boolean default false not null 
);

create table if not exists white_list (
    tg_id integer primary key 
);

insert into white_list (user_id)
values (7131650742);


insert into user (user_id)
values (7131650742);
