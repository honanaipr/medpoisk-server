BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 19f977649fc1

CREATE TABLE division (
    id SERIAL NOT NULL, 
    title TEXT NOT NULL, 
    address TEXT NOT NULL, 
    super_division_id INTEGER, 
    PRIMARY KEY (id), 
    FOREIGN KEY(super_division_id) REFERENCES division (id)
);

CREATE TABLE doctor (
    id SERIAL NOT NULL, 
    name VARCHAR, 
    PRIMARY KEY (id), 
    UNIQUE (name)
);

CREATE TABLE employee (
    id SERIAL NOT NULL, 
    username VARCHAR NOT NULL, 
    first_name TEXT, 
    middle_name TEXT, 
    last_name TEXT NOT NULL, 
    email TEXT, 
    password_hash BYTEA NOT NULL, 
    PRIMARY KEY (id)
);

CREATE TABLE product (
    id SERIAL NOT NULL, 
    title VARCHAR NOT NULL, 
    description VARCHAR, 
    barcode BIGINT, 
    PRIMARY KEY (id), 
    UNIQUE (title)
);

CREATE TABLE minamount (
    id SERIAL NOT NULL, 
    division_id INTEGER NOT NULL, 
    product_id INTEGER NOT NULL, 
    min_amount INTEGER NOT NULL, 
    PRIMARY KEY (id), 
    FOREIGN KEY(division_id) REFERENCES division (id), 
    FOREIGN KEY(product_id) REFERENCES product (id)
);

CREATE TABLE picture (
    id SERIAL NOT NULL, 
    product_id INTEGER NOT NULL, 
    url VARCHAR NOT NULL, 
    PRIMARY KEY (id), 
    FOREIGN KEY(product_id) REFERENCES product (id)
);

CREATE TABLE place (
    id SERIAL NOT NULL, 
    title VARCHAR NOT NULL, 
    division_id INTEGER NOT NULL, 
    PRIMARY KEY (id), 
    FOREIGN KEY(division_id) REFERENCES division (id)
);

CREATE TYPE "ROLE" AS ENUM ('doctor', 'manager', 'director');

CREATE TABLE privilage (
    id SERIAL NOT NULL, 
    employee_id INTEGER NOT NULL, 
    division_id INTEGER NOT NULL, 
    role_name "ROLE" NOT NULL, 
    PRIMARY KEY (id), 
    FOREIGN KEY(division_id) REFERENCES division (id), 
    FOREIGN KEY(employee_id) REFERENCES employee (id)
);

CREATE TABLE room (
    id SERIAL NOT NULL, 
    title VARCHAR NOT NULL, 
    division_id INTEGER NOT NULL, 
    PRIMARY KEY (id), 
    FOREIGN KEY(division_id) REFERENCES division (id)
);

CREATE TABLE inventory (
    id SERIAL NOT NULL, 
    product_id INTEGER NOT NULL, 
    place_id INTEGER NOT NULL, 
    amount INTEGER NOT NULL, 
    PRIMARY KEY (id), 
    FOREIGN KEY(place_id) REFERENCES place (id), 
    FOREIGN KEY(product_id) REFERENCES product (id)
);

CREATE TABLE position (
    id SERIAL NOT NULL, 
    amount INTEGER NOT NULL, 
    place_id INTEGER NOT NULL, 
    product_id INTEGER NOT NULL, 
    PRIMARY KEY (id), 
    FOREIGN KEY(place_id) REFERENCES place (id), 
    FOREIGN KEY(product_id) REFERENCES product (id)
);

INSERT INTO alembic_version (version_num) VALUES ('19f977649fc1') RETURNING alembic_version.version_num;

COMMIT;

