#!/usr/bin/env python3
"""
Module for caching web pages with expiration and tracking
access counts.
"""

import time
import requests
import redis
from functools import wraps

# Initialize the Redis client
cache = redis.Redis()


def cache_page(func):
    """
    Decorator to cache the results of the get_page function and
    count accesses to each URL.
    """
    @wraps(func)
    def wrapper(url: str) -> str:
        # Increment the access count for the URL
        count_key = f"count:{url}"
        cache.incr(count_key)

        # Check if the page is already cached
        cached_page = cache.get(url)
        if cached_page is not None:
            return cached_page.decode()

        # Call the original function to fetch the page
        result = func(url)

        # Cache the result with a 10-second expiration
        cache.setex(url, 10, result)
        return result
    return wrapper


@cache_page
def get_page(url: str) -> str:
    """
    Fetch the HTML content of a specific URL.

    Args:
        url: The URL of the page to retrieve.

    Returns:
        The HTML content of the page.
    """
    time.sleep(5)
    response = requests.get(url)
    return response.text


# For testing
if __name__ == "__main__":
    url_base = "http://slowwly.robertomurray.co.uk/delay/5000/url/"
    url_test = url_base + "http://www.google.com"
    print(get_page(url_test))
    print(get_page(url_test))
    print(cache.get(f"count:{url_test}").decode())
