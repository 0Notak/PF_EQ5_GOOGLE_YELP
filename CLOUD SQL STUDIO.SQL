use pf_henry;
CREATE TABLE IF NOT EXISTS
  business ( business_id VARCHAR (50),
    nombre VARCHAR (30),
    city VARCHAR (20),
    state VARCHAR (20),
    latitude FLOAT,
    longitude FLOAT,
    stars FLOAT,
    review_count FLOAT,
    categories VARCHAR (50)
    );
CREATE TABLE IF NOT EXISTS
  user1 ( user_id VARCHAR (50),
    name VARCHAR (50),
    review_count INTEGER ,
    useful INTEGER,
    funny INTEGER,
    cool INTEGER,
    fans INTEGER,
    average_stars FLOAT
 
    );

CREATE TABLE IF NOT EXISTS
  rev_az ( business_id VARCHAR (50),
    name VARCHAR (50),
    city VARCHAR (25),
    review_count INTEGER,
    user_id INTEGER,
    stars FLOAT,
    useful INTEGER,
    funny INTEGER,
    cool INTEGER,
    fecha DATE,
    `Polaridad del sentimiento` FLOAT,
    Sentimiento INTEGER );
CREATE TABLE IF NOT EXISTS
  rev_fl ( business_id VARCHAR (50),
    name VARCHAR (50),
    city VARCHAR (50),
    review_count INTEGER,
    user_id VARCHAR (50),
    stars INTEGER,
    useful INTEGER,
    funny INTEGER,
    cool INTEGER,
    date DATE,
    `Polaridad del sentimiento` FLOAT,
    Sentimiento INTEGER );
CREATE TABLE IF NOT EXISTS
  rev_ca ( user_id VARCHAR (50),
    business_id VARCHAR (50),
    stars INTEGER,
    useful INTEGER,
    funny INTEGER,
    cool INTEGER,
    date DATE,
    `Polaridad del sentimiento` FLOAT,
    Sentimiento INTEGER,
    ano INTEGER,
    mes INTEGER );

CREATE TABLE IF NOT EXISTS
  tip ( business_id VARCHAR (50),
    user_id VARCHAR (30),
    text VARCHAR (30),
    compliment_count FLOAT
    );