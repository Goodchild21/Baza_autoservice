INSERT INTO Сustumers (firstname, middlename, lastname, phone)
    VALUES('Aleksey', 'Aleksandrovich', 'Batashev', 89534217689),
        ('Ivan', 'Ivanovich', 'Ivanov', 89534217690),
        ('Pedr', 'Pedrovich', 'Shpak', 89534217691);


INSERT INTO Mechanics (id, firstname, middlename, lastname, specialization)
    VALUES(1, 'Koliy', 'Kolich', NULL, 'engine_repair'),
        (2, 'Geka', 'Sipliy', NULL, 'gearbox_repair'),
        (3, 'Michal', 'Michalich', NULL, 'all_questions');

    
INSERT INTO Parts (id, parts, price)
    VALUES(1, 'camshaft х 2', 54000.8),
        (2, 'transmission_oil х 4', 36400.6),
        (3, 'spark_plug х 4', 16400.4);


INSERT INTO Orders (id, type_of_repair, custumer_id, mechanic_id, parts_id, total_price, created_date)
    VALUES(1, replacing camshafts, 1, 1, 1, 70000.8),
        (2, replacing camshafts, 2, 2, 2, 50000.6),
        (3, replacing camshafts, 3, 3, 3, 30000.4);


SELECT *
    FROM Custumers
    ORDER BY lastname;


DELETE
    FROM Orders
    WHERE id = 3