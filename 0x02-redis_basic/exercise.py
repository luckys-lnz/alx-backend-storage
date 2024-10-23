#!/usr/bin/env python3
"""Create a Cache class. In the __init__ method, store an instance
of the Redis client as a private variable named _redis (using redis.
Redis()) and flush the instance using flushdb.

Create a store method that takes a data argument and returns a string.
The method should generate a random key (e.g. using uuid), store the
input data in Redis using the random key and return the key.

Type-annotate store correctly. Remember that data can be a str, bytes,
int or float.
"""

import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """Initialize Redis client and flush the database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a random key"""
        random_key = str(uuid.uuid4())

        # Store the data in Redis using the random key
        self._redis.set(random_key, data)

        # Return the random key
        return random_key