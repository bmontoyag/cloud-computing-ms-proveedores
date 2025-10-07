
-- Esquema y tabla para proveedores
CREATE SCHEMA IF NOT EXISTS proveedores;
CREATE TABLE IF NOT EXISTS proveedores.proveedores (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(160) UNIQUE NOT NULL,
  contacto VARCHAR(160),
  precio_referencia NUMERIC DEFAULT 0
);

INSERT INTO proveedores.proveedores (nombre, contacto, precio_referencia) VALUES
  ('Acero S.A.', 'ventas@acero.com', 1200.50),
  ('Cemento & Cia', 'contacto@cemento.com', 850.00)
ON CONFLICT DO NOTHING;
