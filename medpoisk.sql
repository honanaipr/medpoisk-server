--
-- PostgreSQL database cluster dump
--

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Drop databases (except postgres and template1)
--

DROP DATABASE medpoisk;




--
-- Drop roles
--

DROP ROLE postgres;


--
-- Roles
--

CREATE ROLE postgres;
ALTER ROLE postgres WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS PASSWORD 'SCRAM-SHA-256$4096:/1N06eFaG+OMNp1GVH0O3w==$Gc9kx4VDnY+029myZIeYqTmM4XHFXwdn1mufCIaSXO4=:B0Tl0LcyJhsGwQUzJhNZzZ2TcfdBs1QxFZ/+H1UO7W0=';

--
-- User Configurations
--








--
-- Databases
--

--
-- Database "template1" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0 (Debian 16.0-1.pgdg120+1)
-- Dumped by pg_dump version 16.0 (Debian 16.0-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

UPDATE pg_catalog.pg_database SET datistemplate = false WHERE datname = 'template1';
DROP DATABASE template1;
--
-- Name: template1; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE template1 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';


ALTER DATABASE template1 OWNER TO postgres;

\connect template1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE template1; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE template1 IS 'default template for new databases';


--
-- Name: template1; Type: DATABASE PROPERTIES; Schema: -; Owner: postgres
--

ALTER DATABASE template1 IS_TEMPLATE = true;


\connect template1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE template1; Type: ACL; Schema: -; Owner: postgres
--

REVOKE CONNECT,TEMPORARY ON DATABASE template1 FROM PUBLIC;
GRANT CONNECT ON DATABASE template1 TO PUBLIC;


--
-- PostgreSQL database dump complete
--

--
-- Database "medpoisk" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0 (Debian 16.0-1.pgdg120+1)
-- Dumped by pg_dump version 16.0 (Debian 16.0-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: medpoisk; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE medpoisk WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';


ALTER DATABASE medpoisk OWNER TO postgres;

\connect medpoisk

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: doctors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.doctors (
    id uuid NOT NULL,
    name character varying
);


ALTER TABLE public.doctors OWNER TO postgres;

--
-- Name: places; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.places (
    id uuid NOT NULL,
    title character varying
);


ALTER TABLE public.places OWNER TO postgres;

--
-- Name: positions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.positions (
    id uuid NOT NULL,
    amount integer,
    place_id uuid,
    product_id uuid,
    CONSTRAINT positions_amount_check CHECK ((amount >= 0))
);


ALTER TABLE public.positions OWNER TO postgres;

--
-- Name: products; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.products (
    id uuid NOT NULL,
    title character varying,
    min_amount integer,
    barcode bigint
);


ALTER TABLE public.products OWNER TO postgres;

--
-- Name: rooms; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.rooms (
    id uuid NOT NULL,
    number integer
);


ALTER TABLE public.rooms OWNER TO postgres;

--
-- Data for Name: doctors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.doctors (id, name) FROM stdin;
a1a68ddd-548c-4018-b6ab-43a244522eee	Агафонов Роман Миронович
8daac4a1-07e5-4b16-8884-6a4d6fc6f191	Акимов Павел Михайлович
c98abfcf-01bb-4dc8-8879-d1b8a270945e	Андреева Анастасия Викторовна
49407f86-eebf-4eb5-aa30-9be470f7854e	Анисимова София Михайловна
fe4e8c2d-8f0a-44e6-b2c5-4ac8314f0d40	Антонова София Романовна
\.


--
-- Data for Name: places; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.places (id, title) FROM stdin;
1068a946-2636-4735-90eb-2662c651111f	Шкаф №1
c2eb4241-76ca-4fd3-ab44-c2c29582a02a	Шкаф №2
230a0785-51d5-4b9d-bf5e-cab278c94715	Шкаф №3
c38fa938-19b8-47fb-bbff-6c4371adc40d	Холодильник
36dd05b1-1457-4bcf-8c50-12d99b15d849	Морозильник
\.

--
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.products (id, title, min_amount, barcode) FROM stdin;
f76cae90-e0f5-4f82-a7d5-b14bc044e217	Набор для спинально-эпидуральной анестезии Portex, коробка по 50 шт.	3	12345
1a97ff0c-980c-48d7-aad4-6594b87969fa	Набор для спинально-эпидуральной анестезии Portex, коробка по 5 шт.	1	12346
5e960a2d-0c1c-4ff4-8e40-6a4c2e0491f2	Медиагель - гель для УЗИ высокой вязкости бесцветный, упаковка по 100 шт.	18	12347
7d3a8868-479a-408d-b3db-83908ab52def	Игла спинальная (88мм) SURU для анестезии Квинке, упаковка по 100 шт.	5	12348
7a2e589d-ee70-4a14-9aee-4f4f54ab0b2f	Игла спинальная (88мм) SURU для анестезии Квинке, упаковка по 50 шт.	2	12349
\.

--
-- Data for Name: positions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.positions (id, amount, place_id, product_id) FROM stdin;
d8462567-5a51-4ed8-bcba-bdb770df6370	17	1068a946-2636-4735-90eb-2662c651111f	f76cae90-e0f5-4f82-a7d5-b14bc044e217
d60e7d65-ff88-4287-85b1-957cb899ae93	20	c2eb4241-76ca-4fd3-ab44-c2c29582a02a	1a97ff0c-980c-48d7-aad4-6594b87969fa
65cc787b-5d12-4e5a-9c19-7891446b189b	10	230a0785-51d5-4b9d-bf5e-cab278c94715	5e960a2d-0c1c-4ff4-8e40-6a4c2e0491f2
4030fd80-6c92-401b-b019-3e48a89199b7	12	c38fa938-19b8-47fb-bbff-6c4371adc40d	7d3a8868-479a-408d-b3db-83908ab52def
ca229dfe-4d9f-4523-a6fd-c99834e0dbdc	17	36dd05b1-1457-4bcf-8c50-12d99b15d849	7a2e589d-ee70-4a14-9aee-4f4f54ab0b2f
30e9d7d9-6a0b-45a6-b73c-dab9035a7db3	4	c2eb4241-76ca-4fd3-ab44-c2c29582a02a	7a2e589d-ee70-4a14-9aee-4f4f54ab0b2f
\.

--
-- Data for Name: rooms; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.rooms (id, number) FROM stdin;
eff74e5e-9469-4525-ac5f-5ce306354f6f	13
512c79a1-1c4e-4100-ac8a-d6803e615991	15
abd39888-83d2-4e65-bb58-667f021988e4	1
df6f8fc3-e0c1-4d52-8b34-7b45897c73c4	7
521c3537-486a-4327-8b17-67ed32182c8e	4
\.


--
-- Name: doctors doctors_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.doctors
    ADD CONSTRAINT doctors_name_key UNIQUE (name);


--
-- Name: doctors doctors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.doctors
    ADD CONSTRAINT doctors_pkey PRIMARY KEY (id);


--
-- Name: places places_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.places
    ADD CONSTRAINT places_pkey PRIMARY KEY (id);


--
-- Name: places places_title_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.places
    ADD CONSTRAINT places_title_key UNIQUE (title);


--
-- Name: positions positions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.positions
    ADD CONSTRAINT positions_pkey PRIMARY KEY (id);


--
-- Name: products products_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (id);


--
-- Name: rooms rooms_number_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rooms
    ADD CONSTRAINT rooms_number_key UNIQUE (number);


--
-- Name: rooms rooms_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rooms
    ADD CONSTRAINT rooms_pkey PRIMARY KEY (id);


--
-- Name: positions positions_place_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.positions
    ADD CONSTRAINT positions_place_id_fkey FOREIGN KEY (place_id) REFERENCES public.places(id);


--
-- Name: positions positions_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.positions
    ADD CONSTRAINT positions_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(id);


--
-- PostgreSQL database dump complete
--

--
-- Database "postgres" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0 (Debian 16.0-1.pgdg120+1)
-- Dumped by pg_dump version 16.0 (Debian 16.0-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE postgres;
--
-- Name: postgres; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';


ALTER DATABASE postgres OWNER TO postgres;

\connect postgres

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE postgres; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE postgres IS 'default administrative connection database';


--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database cluster dump complete
--

