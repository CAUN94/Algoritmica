--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.3
-- Dumped by pg_dump version 9.5.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE diet;
--
-- Name: diet; Type: DATABASE; Schema: -; Owner: -
--

CREATE DATABASE diet WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';


\connect diet

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA public;


--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON SCHEMA public IS 'standard public schema';


--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_with_oids = false;

--
-- Name: amounts; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE amounts (
    nutr character varying(4) NOT NULL,
    food character varying(5) NOT NULL,
    amt double precision
);


--
-- Name: foods; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE foods (
    food character varying(5) NOT NULL,
    cost double precision,
    f_min double precision,
    f_max double precision,
    buy double precision,
    buy_rc double precision,
    buy_frac double precision
);


--
-- Name: nutrients; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE nutrients (
    nutr character varying(4) NOT NULL,
    n_min double precision,
    n_max double precision
);


--
-- Data for Name: amounts; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO amounts VALUES ('A', 'BEEF', 60);
INSERT INTO amounts VALUES ('C', 'BEEF', 20);
INSERT INTO amounts VALUES ('B1', 'BEEF', 10);
INSERT INTO amounts VALUES ('B2', 'BEEF', 15);
INSERT INTO amounts VALUES ('NA', 'BEEF', 938);
INSERT INTO amounts VALUES ('CAL', 'BEEF', 295);
INSERT INTO amounts VALUES ('A', 'CHK', 8);
INSERT INTO amounts VALUES ('C', 'CHK', 0);
INSERT INTO amounts VALUES ('B1', 'CHK', 20);
INSERT INTO amounts VALUES ('B2', 'CHK', 20);
INSERT INTO amounts VALUES ('NA', 'CHK', 2180);
INSERT INTO amounts VALUES ('CAL', 'CHK', 770);
INSERT INTO amounts VALUES ('A', 'FISH', 8);
INSERT INTO amounts VALUES ('C', 'FISH', 10);
INSERT INTO amounts VALUES ('B1', 'FISH', 15);
INSERT INTO amounts VALUES ('B2', 'FISH', 10);
INSERT INTO amounts VALUES ('NA', 'FISH', 945);
INSERT INTO amounts VALUES ('CAL', 'FISH', 440);
INSERT INTO amounts VALUES ('A', 'HAM', 40);
INSERT INTO amounts VALUES ('C', 'HAM', 40);
INSERT INTO amounts VALUES ('B1', 'HAM', 35);
INSERT INTO amounts VALUES ('B2', 'HAM', 10);
INSERT INTO amounts VALUES ('NA', 'HAM', 278);
INSERT INTO amounts VALUES ('CAL', 'HAM', 430);
INSERT INTO amounts VALUES ('A', 'MCH', 15);
INSERT INTO amounts VALUES ('C', 'MCH', 35);
INSERT INTO amounts VALUES ('B1', 'MCH', 15);
INSERT INTO amounts VALUES ('B2', 'MCH', 15);
INSERT INTO amounts VALUES ('NA', 'MCH', 1182);
INSERT INTO amounts VALUES ('CAL', 'MCH', 315);
INSERT INTO amounts VALUES ('A', 'MTL', 70);
INSERT INTO amounts VALUES ('C', 'MTL', 30);
INSERT INTO amounts VALUES ('B1', 'MTL', 15);
INSERT INTO amounts VALUES ('B2', 'MTL', 15);
INSERT INTO amounts VALUES ('NA', 'MTL', 896);
INSERT INTO amounts VALUES ('CAL', 'MTL', 400);
INSERT INTO amounts VALUES ('A', 'SPG', 25);
INSERT INTO amounts VALUES ('C', 'SPG', 50);
INSERT INTO amounts VALUES ('B1', 'SPG', 25);
INSERT INTO amounts VALUES ('B2', 'SPG', 15);
INSERT INTO amounts VALUES ('NA', 'SPG', 1329);
INSERT INTO amounts VALUES ('CAL', 'SPG', 370);
INSERT INTO amounts VALUES ('A', 'TUR', 60);
INSERT INTO amounts VALUES ('C', 'TUR', 20);
INSERT INTO amounts VALUES ('B1', 'TUR', 15);
INSERT INTO amounts VALUES ('B2', 'TUR', 10);
INSERT INTO amounts VALUES ('NA', 'TUR', 1397);
INSERT INTO amounts VALUES ('CAL', 'TUR', 450);


--
-- Data for Name: foods; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO foods VALUES ('BEEF', 3.18999999999999995, 2, 10, NULL, NULL, NULL);
INSERT INTO foods VALUES ('CHK', 2.58999999999999986, 2, 10, NULL, NULL, NULL);
INSERT INTO foods VALUES ('FISH', 2.29000000000000004, 2, 10, NULL, NULL, NULL);
INSERT INTO foods VALUES ('HAM', 2.89000000000000012, 2, 10, NULL, NULL, NULL);
INSERT INTO foods VALUES ('MCH', 1.8899999999999999, 2, 10, NULL, NULL, NULL);
INSERT INTO foods VALUES ('MTL', 1.98999999999999999, 2, 10, NULL, NULL, NULL);
INSERT INTO foods VALUES ('SPG', 1.98999999999999999, 2, 10, NULL, NULL, NULL);
INSERT INTO foods VALUES ('TUR', 2.49000000000000021, 2, 10, NULL, NULL, NULL);


--
-- Data for Name: nutrients; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO nutrients VALUES ('A', 700, 20000);
INSERT INTO nutrients VALUES ('C', 700, 20000);
INSERT INTO nutrients VALUES ('B1', 700, 20000);
INSERT INTO nutrients VALUES ('B2', 700, 20000);
INSERT INTO nutrients VALUES ('NA', 0, 50000);
INSERT INTO nutrients VALUES ('CAL', 16000, 24000);


--
-- Name: amounts_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY amounts
    ADD CONSTRAINT amounts_pk PRIMARY KEY (nutr, food);


--
-- Name: foods_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY foods
    ADD CONSTRAINT foods_pk PRIMARY KEY (food);


--
-- Name: nutrients_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY nutrients
    ADD CONSTRAINT nutrients_pk PRIMARY KEY (nutr);


--
-- PostgreSQL database dump complete
--

