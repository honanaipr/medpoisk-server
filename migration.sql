BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 87e34954be29

CREATE TABLE doctors (
    id UUID NOT NULL, 
    name VARCHAR, 
    PRIMARY KEY (id), 
    UNIQUE (name)
);

CREATE TABLE places (
    id UUID NOT NULL, 
    title VARCHAR, 
    PRIMARY KEY (id), 
    UNIQUE (title)
);

CREATE TABLE products (
    id UUID NOT NULL, 
    title VARCHAR, 
    min_amount INTEGER, 
    barcode BIGINT, 
    PRIMARY KEY (id)
);

CREATE TABLE rooms (
    id UUID NOT NULL, 
    number INTEGER, 
    PRIMARY KEY (id), 
    UNIQUE (number)
);

CREATE TABLE positions (
    id UUID NOT NULL, 
    amount INTEGER NOT NULL, 
    place_id UUID NOT NULL, 
    product_id UUID NOT NULL, 
    PRIMARY KEY (id), 
    FOREIGN KEY(place_id) REFERENCES places (id), 
    FOREIGN KEY(product_id) REFERENCES products (id)
);

INSERT INTO alembic_version (version_num) VALUES ('87e34954be29') RETURNING alembic_version.version_num;

-- Running upgrade 87e34954be29 -> 915d27de520b

ALTER TABLE products ADD COLUMN picture_url VARCHAR;

UPDATE alembic_version SET version_num='915d27de520b' WHERE alembic_version.version_num = '87e34954be29';

COMMIT;

