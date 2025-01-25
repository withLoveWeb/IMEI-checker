create table if not exists "user" (
    user_id bigserial primary key,
    encrypted_token varchar unique not null,
    is_admin boolean default false not null 
);

create table if not exists white_list (
    tg_id integer primary key 
);

insert into white_list (user_id)
values (7131650742);


insert into "user" (user_id, encrypted_token, is_admin)
values (7131650742, 'flkasj', True);
