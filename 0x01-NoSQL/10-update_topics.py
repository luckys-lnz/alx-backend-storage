#!/usr/bin/env python3
"""Module to update topics of a school document."""

from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.

    Parameters:
    mongo_collection: The pymongo collection object.
    name (str): The school name to update.
    topics (list of str): The list of topics approached in the school.
    
    Returns:
    None
    """
    mongo_collection.update_many(
        {"name": name},  # Filter documents by school name
        {"$set": {"topics": topics}}  # Set the new list of topics
    )

