SELECT *
    FROM Custumers
    JOIN Mechanics ON Custumers.firstname=Mechanics.firstname;


SELECT *
    FROM Mechanics
    CROSS JOIN Parts;


CREATE UNIQUE INDEX Parts_id_index ON Parts(id);
CREATE INDEX Custumers_id_index ON Custumers(id)
    WHERE id > 2;


DROP INDEX Parts_id_index;
DROP INDEX Custumers_id_index;
