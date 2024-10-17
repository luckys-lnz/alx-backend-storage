-- SQL script that creates a trigger

-- Sets custom delimiter
DELIMITER |

CREATE TRIGGER reset_valid_email BEFORE UPDATE
ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END |

-- Restore defualt delimiter
DELIMITER ;