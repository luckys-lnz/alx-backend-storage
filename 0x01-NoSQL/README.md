# NoSQL Databases & MongoDB

## What is NoSQL?

NoSQL stands for Not Only SQL. It refers to a class of databases that are designed to handle a wide variety of data types and do not necessarily use relational database management principles. NoSQL databases provide a mechanism for storage and retrieval of data that is modeled in means other than the tabular relations used in SQL databases.

Difference Between SQL and NoSQL

| Feature          | SQL                                                        | NoSQL                                                 |
| ---------------- | ---------------------------------------------------------- | ----------------------------------------------------- |
| **Data Model**   | Relational (tables with rows & columns)                    | Non-relational (key-value, document, etc.)            |
| **Schema**       | Fixed schema                                               | Dynamic schema                                        |
| **Scalability**  | Vertical (scaling by adding more power to a single server) | Horizontal (scaling by adding more servers)           |
| **Transactions** | Supports ACID transactions                                 | Some support ACID, but typically eventual consistency |
| **Use Case**     | Best for structured data and complex queries               | Best for unstructured and semi-structured data        |

## What is ACID?

ACID is a set of properties that ensure reliable transaction processing in databases:

1. Atomicity: Transactions are all-or-nothing. If one part of a transaction fails, the entire transaction fails.
2. Consistency: Ensures that a transaction brings the database from one valid state to another valid state.
3. Isolation: Transactions occur independently of one another.
4. Durability: Once a transaction is committed, it remains so, even in the case of a system failure.

## What is Document Storage?

Document storage refers to storing data in document-oriented databases where data is stored in the form of documents. These documents are usually encoded in JSON, BSON, or XML formats. Each document can have different fields, unlike relational databases where every row in a table must follow the same structure.

## Types of NoSQL Databases

1. Document Databases: Store data as JSON-like documents (e.g., MongoDB).
2. Key-Value Stores: Store data as key-value pairs (e.g., Redis, DynamoDB).
3. Wide-Column Stores: Use tables, rows, and dynamic columns (e.g., Cassandra, HBase).
4. Graph Databases: Store relationships between entities as nodes and edges (e.g., Neo4j).

## Benefits of NoSQL Databases

1. Flexibility: NoSQL databases allow dynamic schemas, making it easier to manage changing data structures.
2. Scalability: These databases are designed for horizontal scaling across multiple servers.
3. Performance: NoSQL can handle large volumes of unstructured data and deliver high performance on big data workloads.
4. High Availability: Many NoSQL databases are designed for distributed systems, ensuring high availability and fault tolerance.

## Querying Information from a NoSQL Database

In NoSQL databases like MongoDB, you query data differently from SQL. Here's an example of querying documents in MongoDB:

```
// Find all documents in a collection
db.collection.find({});

// Find documents matching certain criteria
db.collection.find({ "age": { $gt: 25 } });
```

### Common Query Operators in NoSQL (MongoDB)

- $gt, $lt: Greater than, Less than
- $in: Matches any of the values specified in an array
- $and, $or: Logical AND, OR

## Inserting, Updating, and Deleting Information from a NoSQL Database

**Insert Data**

```
// Insert a single document
db.collection.insertOne({ name: "John", age: 30 });

// Insert multiple documents
db.collection.insertMany([{ name: "Alice", age: 25 }, { name: "Bob", age: 28 }]);
```

**Update Data:**

```
// Update one document
db.collection.updateOne({ name: "John" }, { $set: { age: 31 } });

// Update multiple documents
db.collection.updateMany({ age: { $lt: 30 } }, { $set: { status: "young" } });
```

**Delete Data:**

```
// Delete one document
db.collection.deleteOne({ name: "John" });

// Delete multiple documents
db.collection.deleteMany({ age: { $gt: 30 } });
```

## Getting Started with MongoDB

1. **Install MongoDB**: You can install MongoDB locally or use a cloud provider like MongoDB Atlas.

- Install locally on your machine:
  ```
  brew tap mongodb/brew
  brew install mongodb-community
  ```

2. **Set up a MongoDB project**: Use the mongo shell or integrate MongoDB into your application using a driver like mongoose for Node.js.
   ```
   npm install mongoose
   ```

Basic connection in your app:

```
const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost:27017/mydatabase', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});
```

3. Create Collections: In MongoDB, collections are similar to tables in SQL. Documents are inserted into collections.

```
const userSchema = new mongoose.Schema({
  name: String,
  age: Number
});

const User = mongoose.model('User', userSchema);

// Inserting a document
User.create({ name: 'John', age: 30 });
```

# Conclusion

This overview covers basic syntax and benefits of NoSQL and mongoDB basic syntax.

### Learn More

- [NoSQL](https://riak.com/resources/nosql-databases/)
- [MongoDB Tutorial 2 : Insert, Update, Remove, Query](https://www.youtube.com/watch?v=CB9G5Dvv-EE)
- [Aggregation Operations](https://www.mongodb.com/docs/manual/aggregation/)
- [Mongosh](https://www.mongodb.com/docs/mongodb-shell/#mongodb-binary-bin.mongosh)
- [MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/)
- [Mongo shell methods](https://www.mongodb.com/docs/manual/reference/method/)