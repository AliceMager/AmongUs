create schema amongus;

create type status as enum (
  'CREATED',
  'DELETED'
);

create table amongus.deployment(
    id UUID PRIMARY KEY DEFAULT (gen_random_uuid()),
    db_name VARCHAR NOT null,
    status status NOT null,
    username VARCHAR NOT null,
    creation_time timestamp without time zone not null default (current_timestamp at time zone 'utc')
);