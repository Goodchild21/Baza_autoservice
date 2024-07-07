BEGIN
INSERT INTO Custumers (id, firstname, middlename, lastname, phone)
    VALUES (4, 'Pedr', 'Pedrovich', 'Shpak', '89534217691');

SAVEPOINT after_insert;

UPDATE Custumers
    SET lastname = 'Pedorov'
    WHERE id = 4;

ROLLBACK after_insert;
COMMIT;
