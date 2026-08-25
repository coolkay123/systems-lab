CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price_cents INTEGER NOT NULL CHECK (price_cents >= 0),
    in_stock INTEGER NOT NULL CHECK (in_stock IN (0, 1))
);

INSERT INTO products (name, category, price_cents, in_stock) VALUES
    ('Mechanical Keyboard', 'peripherals', 8900, 1),
    ('USB-C Cable',         'accessories', 1200, 1),
    ('27-inch Monitor',     'displays',   24900, 0),
    ('Wireless Mouse',      'peripherals', 4500, 1),
    ('Laptop Stand',       'accessories', 3900, 1),
    ('Webcam',              'peripherals', 6900, 0);

