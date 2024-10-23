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
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count calls to a method using Redis."""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Increment the call count and call the original method."""
        key = method.__qualname__
        self._redis.incr(key)  # Increment the call count in Redis
        return method(self, *args, **kwargs)  # Call the original method

    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs in Redis."""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Append input and output to Redis lists."""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Append the string representation of arguments to the inputs list
        self._redis.rpush(input_key, str(args))

        # Call the original method and retrieve the output
        output = method(self, *args, **kwargs)

        # Append the output to the outputs list
        self._redis.rpush(output_key, output)

        return output

    return wrapper


class Cache:
    def __init__(self):
        """Initialize Redis client and flush the database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a random key"""
        random_key = str(uuid.uuid4())

        # Store the data in Redis using the random key
        self._redis.set(random_key, data)

        # Return the random key
        return random_key

    def get(self, key: str, fn: Optional[Callable] = None
            ) -> Optional[Union[str, int, float]]:
        """Retrieve value from redisa and convert it using Callable"""
        value = self._redis.get(key)

        if value is None:
            return None

        if fn:
            return fn(value)

        return value

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve a string value from Redis."""
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve an integer value from Redis."""
        return self.get(key, int)

def replay(method: Callable):
    """Display the history of calls to a particular method."""
    key = method.__qualname__
    call_count = method.__self__._redis.get(key).decode('utf-8')
    inputs = method.__self__._redis.lrange(f"{key}:inputs", 0, -1)
    outputs = method.__self__._redis.lrange(f"{key}:outputs", 0, -1)

    print(f"{key} was called {call_count} times:")

    for input_data, output_data in zip(inputs, outputs):
        # Decode input and output for better readability
        input_args = eval(input_data.decode('utf-8'))
        output_value = output_data.decode('utf-8')
        print(f"{key}(*{input_args}) -> {output_value}")
