DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS booking_confirmations;
DROP TABLE IF EXISTS services;
DROP TABLE IF EXISTS photographers;
DROP TABLE IF EXISTS clients;

CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    client_from VARCHAR(255),
    email VARCHAR(255),
    birthdate INT,
    contact VARCHAR(255)
);


CREATE TABLE photographers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    portfolio_address VARCHAR(255)
); 

CREATE TABLE services (
    id SERIAL PRIMARY KEY,
    photo_type VARCHAR(255),
    hours INT,
    price INT
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    places TEXT,
    -- places text,
    num_of_group INT,
    photoshoot_start_time TIMESTAMP,
    photoshoot_end_time TIMESTAMP,
    client_id SERIAL REFERENCES clients(id) ON DELETE CASCADE,
    service_id SERIAL REFERENCES services(id) ON DELETE CASCADE,    
    photographer_id SERIAL REFERENCES photographers(id) ON DELETE CASCADE
);

CREATE TABLE booking_confirmations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    places TEXT,
    -- places text,
    num_of_group INT,
    photoshoot_start_time TIMESTAMP,
    photoshoot_end_time TIMESTAMP,
    client_id SERIAL REFERENCES clients(id) ON DELETE CASCADE,
    service_id SERIAL REFERENCES services(id) ON DELETE CASCADE,    
    photographer_id SERIAL REFERENCES photographers(id) ON DELETE CASCADE
);

-- CREATE TABLE Places
--     id 
--     booking_id 