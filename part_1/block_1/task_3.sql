CREATE TABLE Сustumers --Клиенты
(
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL,
    phone VARCHAR(11) NOT NULL UNIQUE
);


CREATE TABLE Mechanics --Мастера
(
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    middle_name TEXT NOT NULL,
    last_name TEXT,
    specialization VARCHAR(50) NOT NULL
);


CREATE TABLE Parts --Запчасти
(
    id SERIAL PRIMARY KEY,
    parts TEXT,
    price FLOAT
);


CREATE TABLE Orders --Заказы
(
    id SERIAL PRIMARY KEY,
    type_of_repair TEXT,
    custumer_id INT,
    mechanic_id INT,
    parts_id INT,
    total_price FLOAT,
    created_date DATE DEFAULT current_date,

    FOREIGN KEY (custumer_id) REFERENCES Custumers(id),
    FOREIGN KEY (master_id) REFERENCES Mechanics(id),
    FOREIGN KEY (parts_id) REFERENCES Parts(id)
);
