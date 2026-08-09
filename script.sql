




-- 1. CREACIÓN DE TABLAS (Estructura básica)
CREATE TABLE propietarios (
    id SERIAL,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    telefono VARCHAR(20),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE DATABASE db_veterinaria;
USE db_veterinaria;

CREATE TABLE propietarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    telefono VARCHAR(20) UNIQUE,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE mascotas (
    id SERIAL PRIMARY KEY,
    propietario_id INT REFERENCES propietarios(id) ON DELETE CASCADE,
    nombre VARCHAR(50) NOT NULL,
    especie VARCHAR(30) NOT NULL,
    edad_meses INT CHECK (edad_meses >= 0),
    peso_kg NUMERIC(5,2) CHECK (peso_kg > 0),
    chip_identificador VARCHAR(50) UNIQUE,
    fecha_nacimiento DATE
);


----- Creacion de tablas con constrainst-----
CREATE TABLE mascotas (
    id SERIAL,
    propietario_id INT,
    nombre VARCHAR(50) NOT NULL,
    especie VARCHAR(30) NOT NULL,
    edad_meses INT,
    peso_kg NUMERIC(5,2),
    chip_identificador VARCHAR(50),
    fecha_nacimiento DATE
);

-- 2. AGREGAR RESTRICCIONES CON ALTER TABLE

-- Restricciones para la tabla 'propietarios'
ALTER TABLE propietarios 
    ADD CONSTRAINT pk_propietarios PRIMARY KEY (id);

ALTER TABLE propietarios 
    ADD CONSTRAINT uq_propietarios_email UNIQUE (email);

ALTER TABLE propietarios 
    ADD CONSTRAINT uq_propietarios_telefono UNIQUE (telefono);


-- Restricciones para la tabla 'mascotas'
ALTER TABLE mascotas 
    ADD CONSTRAINT pk_mascotas PRIMARY KEY (id);

ALTER TABLE mascotas 
    ADD CONSTRAINT fk_mascotas_propietario 
    FOREIGN KEY (propietario_id) REFERENCES propietarios(id) ON DELETE CASCADE;

ALTER TABLE mascotas 
    ADD CONSTRAINT uq_mascotas_chip UNIQUE (chip_identificador);

ALTER TABLE mascotas 
    ADD CONSTRAINT chk_mascotas_edad CHECK (edad_meses >= 0);

ALTER TABLE mascotas 
    ADD CONSTRAINT chk_mascotas_peso CHECK (peso_kg > 0);

-- Inserción de varios propietarios en una sola sentencia
INSERT INTO propietarios (nombre, email, telefono) VALUES
('Carlos Gómez', 'carlos.gomez@email.com', '+541198765432'),
('María Rodríguez', 'maria.rod@email.com', '+541187654321'),
('Ana Martínez', 'ana.mar@email.com', '+541176543210'),
('Lucas Pérez', 'lucas.p@email.com', NULL); -- Permite NULL si no es UNIQUE ocupado

-- Inserción de varias mascotas asociadas a los propietarios anteriores
INSERT INTO mascotas (propietario_id, nombre, especie, edad_meses, peso_kg, chip_identificador, fecha_nacimiento) VALUES
(1, 'Firulais', 'Perro', 36, 12.50, 'CHIP-12345', '2023-05-10'),
(1, 'Michi', 'Gato', 12, 4.20, 'CHIP-67890', '2025-02-15'),
(2, 'Rex', 'Perro', 60, 32.10, 'CHIP-11223', '2021-08-20'),
(3, 'Luna', 'Gato', 8, 2.80, NULL, '2025-11-01');