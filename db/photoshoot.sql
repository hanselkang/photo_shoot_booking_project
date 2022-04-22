DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS services;
DROP TABLE IF EXISTS photographers;
DROP TABLE IF EXISTS clients;

CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    client_from VARCHAR(255),
    email VARCHAR(255),
    age INT,
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
    place VARCHAR(255),
    hours INT,
    price INT,
    photographer_id INT NULL REFERENCES photographers(id) ON DELETE CASCADE
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    num_of_group INT,
    client_id INT NULL REFERENCES clients(id) ON DELETE CASCADE,
    service_id INT NULL REFERENCES services(id) ON DELETE CASCADE,
    photographer_id INT NULL REFERENCES photographers(id) ON DELETE CASCADE
);