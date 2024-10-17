-- script that creates a function SafeDiv that
-- divides (and returns) the first by the second number or
-- returns 0 if the second number is equal to 0.

-- Drop function if already exists
DROP FUNCTION IF EXISTS SafeDiv;

-- Sets a custom delimiter
DELIMITER |

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    DECLARE result FLOAT;
    IF b = 0 THEN
        SET result = 0;
        RETURN result;
    ELSE
        SET result = a / b;
        RETURN result;
    END IF;
END |

-- Restores default delimiter
DELIMITER ;