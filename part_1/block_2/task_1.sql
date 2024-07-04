INSERT INTO Сustumers (firstname, middlename, lastname, phone)
    VALUES('Aleksey', 'Aleksandrovich', 'Batashev', '89534217689'),
        ('Ivan', 'Ivanovich', 'Ivanov', '89534217690'),
        ('Pedr', 'Pedrovich', 'Shpak', '89534217691');


INSERT INTO Mechanics (firstname, middlename, lastname, specialization)
    VALUES('Koliy', 'Kolich', NULL, 'engine_repair'),
        ('Geka', 'Sipliy', NULL, 'gearbox_repair'),
        ('Michal', 'Michalich', NULL, 'all_questions');

    
INSERT INTO Parts (parts, price)
    VALUES('camshaft х 2', 54000.8),
        ('transmission_oil х 4', 36400.6),
        ('spark_plug х 4', 16400.4);


INSERT INTO Orders (type_of_repair, custumer_id, mechanic_id, parts_id, total_price, created_date)
    VALUES('replacing camshafts', 1, 1, 1, 70000.8),
        ('replacing camshafts', 2, 2, 2, 50000.6),
        ('replacing camshafts', 3, 3, 3, 30000.4);
