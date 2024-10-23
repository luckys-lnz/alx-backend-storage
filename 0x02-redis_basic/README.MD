# Redis Operations and Caching

## Overview

This project provides a basic introduction to Redis, focusing on two key aspects:

    1. Performing basic operations in Redis.
    2. Using Redis as a simple caching mechanism.

Redis is an in-memory data structure store, commonly used as a database, cache, and message broker. This project will guide you through the steps of setting up and using Redis for basic CRUD operations and caching.

## Prerequisites

Before starting, ensure you have the following installed:

- **Redis**
- Node.js (for any Node.js-related examples or scripts)
- Redis client (e.g., **redis-cli**, **ioredis** for Node.js)

### Project Structure

/redis-basics
├── basic-operations.js # Basic CRUD operations in Redis

    ├── caching-example.js       # Simple caching example using Redis

    ├── README.md                # Project documentation (this file)

    └── package.json             # Node.js project dependencies and scripts (if applicable)

## Basic Redis Operations

Redis supports a variety of basic operations such as SET, GET, DEL, and more. Below are the common operations you can perform:

- Set a key-value pair:

```
redis-cli SET key "value"
```

- Get a value by key:

```
Get a value by key:
```

- Delete a key:

```
redis-cli DEL key
```

## Using Redis as a Cache

Redis is widely used as a caching solution due to its in-memory storage and fast access times. Here's how to use it as a simple cache:

- Set up a TTL (Time to Live):

You can set a key with an expiration time (TTL) to cache data for a limited time:

```
redis-cli SETEX cacheKey 3600 "cachedValue"
```

- Retrieve the cached data:

Fetch the cached value using the key:

```
redis-cli GET cacheKey
```

For a more detailed caching example, check out the caching-example.js file in the project.

### Scripts

If using Node.js, add these scripts to your package.json for easy testing:

```
"scripts": {
  "start": "node basic-operations.js",
  "cache": "node caching-example.js"
}
```

Run these commands to test Redis operations:

```
npm run start     # Runs basic operations script
npm run cache     # Runs caching example script
```

## References

- [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)
- [Redis commands](https://redis.io/docs/latest/commands/)
- [Redis python client ](https://redis-py.readthedocs.io/en/stable/)
- [How to Use Redis With Python ](https://realpython.com/python-redis/)
