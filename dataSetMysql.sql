CREATE DATABASE dbMySQL;

USE dbMySQL;

CREATE TABLE usuarios (
id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(100),
email VARCHAR(100),
fecha_creacion DATETIME
);

INSERT INTO usuarios (nombre, email, fecha_creacion) VALUES ('Juan Pérez', 'juan.perez@example.com', '2023-01-01 10:00:00');
INSERT INTO usuarios (nombre, email, fecha_creacion) VALUES ('Ana Gómez', 'ana.gomez@example.com', '2023-01-02 11:00:00');
INSERT INTO usuarios (nombre, email, fecha_creacion) VALUES ('Luis Martínez', 'luis.martinez@example.com', '2023-01-03 12:00:00');
INSERT INTO usuarios (nombre, email, fecha_creacion) VALUES ('María López', 'maria.lopez@example.com', '2023-01-04 13:00:00');
INSERT INTO usuarios (nombre, email, fecha_creacion) VALUES ('Pedro Sánchez', 'pedro.sanchez@example.com', '2023-01-05 14:00:00');
INSERT INTO usuarios (nombre, email, fecha_creacion) VALUES ('Laura Torres', 'laura.torres@example.com', '2023-01-06 15:00:00');
INSERT INTO usuarios (nombre, email, fecha_creacion) VALUES ('Javier Ruiz', 'javier.ruiz@example.com', '2023-01-07 16:00:00');
INSERT INTO usuarios (nombre, email, fecha_creacion) VALUES ('Claudia Morales', 'claudia.morales@example.com', '2023-01-08 17:00:00');
INSERT INTO usuarios (nombre, email, fecha_creacion) VALUES ('Andrés Fernández', 'andres.fernandez@example.com', '2023-01-09 18:00:00');
INSERT INTO usuarios (nombre, email, fecha_creacion) VALUES ('Sofía Jiménez', 'sofia.jimenez@example.com', '2023-01-10 19:00:00');
