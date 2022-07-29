DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS keys;
DROP TABLE IF EXISTS rooms;

CREATE TABLE users (
    id serial PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(50) NOT NULL,
    access INTEGER,
	created_on TIMESTAMP NOT NULL,
    last_login TIMESTAMP
);

CREATE TABLE keys (
    id serial PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
    -- room = Column(Integer, ForeignKey('room.id'))
    -- user = Column(Integer, ForeignKey('user.id'))
);


CREATE TABLE rooms (
    id serial PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);
