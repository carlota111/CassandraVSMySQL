CREATE KEYSPACE IF NOT EXISTS mi_keyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

USE mi_keyspace;
CREATE TABLE usuarios (
    id UUID PRIMARY KEY,
    nombre TEXT,
    email TEXT,
    fecha_creacion TIMESTAMP
);
INSERT INTO usuarios (id, nombre, email, fecha_creacion) VALUES (uuid(), 'Juan Pérez', 'juan.perez@example.com', '2023-01-01 10:00:00');
INSERT INTO usuarios (id, nombre, email, fecha_creacion) VALUES (uuid(), 'Ana Gómez', 'ana.gomez@example.com', '2023-01-02 11:00:00');
INSERT INTO usuarios (id, nombre, email, fecha_creacion) VALUES (uuid(), 'Luis Martínez', 'luis.martinez@example.com', '2023-01-03 12:00:00');
INSERT INTO usuarios (id, nombre, email, fecha_creacion) VALUES (uuid(), 'María López', 'maria.lopez@example.com', '2023-01-04 13:00:00');
INSERT INTO usuarios (id, nombre, email, fecha_creacion) VALUES (uuid(), 'Pedro Sánchez', 'pedro.sanchez@example.com', '2023-01-05 14:00:00');
INSERT INTO usuarios (id, nombre, email, fecha_creacion) VALUES (uuid(), 'Laura Torres', 'laura.torres@example.com', '2023-01-06 15:00:00');
INSERT INTO usuarios (id, nombre, email, fecha_creacion) VALUES (uuid(), 'Javier Ruiz', 'javier.ruiz@example.com', '2023-01-07 16:00:00');
INSERT INTO usuarios (id, nombre, email, fecha_creacion) VALUES (uuid(), 'Claudia Morales', 'claudia.morales@example.com', '2023-01-08 17:00:00');
INSERT INTO usuarios (id, nombre, email, fecha_creacion) VALUES (uuid(), 'Andrés Fernández', 'andres.fernandez@example.com', '2023-01-09 18:00:00');
INSERT INTO usuarios (id, nombre, email, fecha_creacion) VALUES (uuid(), 'Sofía Jiménez', 'sofia.jimenez@example.com', '2023-01-10 19:00:00');

