# MySQL Advanced Concepts

This guide provides an overview of advanced MySQL concepts, including creating tables with constraints, optimizing queries, and implementing stored procedures, functions, views, and triggers

## 1. Creating Tables with Constraints

### What are Constraints?

Constraints are rules enforced on the data columns of a table. They help ensure the accuracy and reliability of the data. Common constraints include:

- **PRIMARY KEY:** Uniquely identifies each record in the table.
- **FOREIGN KEY:** Links one table to another.
- **UNIQUE:** Ensures all values in a column are unique.
- **NOT NULL:** Ensures that a column cannot have a NULL value.
- **CHECK:** Ensures that all values in a column satisfy a specific condition.

Example: Creating a Table with Constraints

```
CREATE TABLE students (
    id INT AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    age INT CHECK (age >= 18),
    email VARCHAR(100) UNIQUE,
    PRIMARY KEY (id)
);
```

In this example:

**PRIMARY KEY** ensures that each student has a unique ID.
**NOT NULL** ensures that the name column cannot be empty.
**CHECK** ensures that only students 18 years or older are allowed.
**UNIQUE** ensures no duplicate email addresses.

## 2. Optimizing Queries with Indexes

### What are Indexes?

Indexes are used to speed up searches and queries by allowing MySQL to find records faster. Indexes can be created on one or more columns.

Example: Adding an Index

```
CREATE INDEX idx_student_name ON students(name);
```

In this example, the index idx_student_name helps MySQL quickly find students by their name, improving query performance.

B**est Practices for Indexing**

- Add indexes to columns used in **WHERE**, **JOIN**, or **ORDER BY** clauses.
- Avoid over-indexing as it can slow down insert and update operations.

## 3. Stored Procedures and Functions

### What are Stored Procedures and Functions?

- Stored Procedures are reusable SQL code blocks that perform a task. They are often used for operations like data validation or batch processing.
- Functions are similar to stored procedures but return a value and can be used in SQL statements.

  Example: Creating a Stored Procedure

  ```
  DELIMITER $$
  CREATE PROCEDURE GetStudent(IN studentId INT)
  BEGIN
    SELECT * FROM students WHERE id = studentId;
  END$$
  DELIMITER ;
  ```

Example: Creating a Function

```
DELIMITER $$
CREATE FUNCTION GetStudentEmail(studentId INT) RETURNS VARCHAR(100)
BEGIN
    DECLARE studentEmail VARCHAR(100);
    SELECT email INTO studentEmail FROM students WHERE id = studentId;
    RETURN studentEmail;
END$$
DELIMITER ;
```

In the above examples:

- The stored procedure **GetStudent** retrieves the student details based on the provided ID.
- The function **GetStudentEmail** returns the email of the student with the provided ID.

## 4. Views in MySQL

### What are Views?

A view is a virtual table based on the result of a query. It can simplify complex queries and improve security by limiting access to certain data.

Example: Creating a View

```
CREATE VIEW student_overview AS
SELECT id, name, email FROM students;
```

In this example, the view **student_overview** shows only the **id**, **name**, and **email** fields from the **students** table, hiding other details like age.

**Benefits of Using Views**

- Simplify complex queries.
- Provide security by exposing only specific data.
- Provide a level of abstraction over your data.

## 5. Triggers in MySQL

### What are Triggers?

Triggers are SQL code that is automatically executed in response to certain events on a table (e.g., INSERT, UPDATE, DELETE).

Example: Creating a Trigger

```
CREATE TRIGGER before_student_insert
BEFORE INSERT ON students
FOR EACH ROW
BEGIN
    IF NEW.age < 18 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Age must be 18 or older';
    END IF;
END;
```

In this example, the trigger **before_student_insert** prevents the insertion of any student whose age is less than 18.

**Types of Triggers**

- BEFORE: Trigger runs before the event (e.g., before inserting data).
- AFTER: Trigger runs after the event (e.g., after updating data).

# Conclusion

This guide covers essential MySQL features that allow you to work with data in a more powerful and efficient manner. By using constraints, indexes, stored procedures, views, and triggers, you can create more secure, optimized, and maintainable databases.

### Learn More

- [MySQL cheatsheet](https://devhints.io/mysql)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://www.liquidweb.com/blog/mysql-optimization-how-to-leverage-mysql-database-indexing/)
- [Stored Procedure](https://www.w3resource.com/mysql/mysql-procedure.php)
- [triggers](https://www.w3resource.com/mysql/mysql-triggers.php)
- [views](https://www.w3resource.com/mysql/mysql-views.php)
- [functions](https://dev.mysql.com/doc/refman/5.7/en/functions.html)
- [trigger syntax](https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html)
- [CREATE PROCEDURE and CREATE table Statements](https://dev.mysql.com/doc/refman/5.7/en/create-table.html)
- [CREATE PROCEDURE and CREATE procedure ](https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html)
- [Index statement](https://dev.mysql.com/doc/refman/5.7/en/create-index.html)
- [Create view statement](https://dev.mysql.com/doc/refman/5.7/en/create-view.html)
