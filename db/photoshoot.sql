DROP TABLE IF EXISTS photographers;
DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS services;

CREATE TABLE services (
    id SERIAL PRIMARY KEY,
    photo_type VARCHAR(255),
    place VARCHAR(255),
    hours INT,
    price INT
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    num_of_group INT,
    service_id INT NULL REFERENCES services(id)
);

CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age VARCHAR(255),
    client_from VARCHAR(255),
    email VARCHAR(255),
    contact VARCHAR(255),
    booking_id INT NULL REFERENCES bookings(id)
);

CREATE TABLE photographers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    portfolio_address VARCHAR(255),
    client_id INT NULL REFERENCES clients(id),
    service_id INT NULL REFERENCES services(id)
);







