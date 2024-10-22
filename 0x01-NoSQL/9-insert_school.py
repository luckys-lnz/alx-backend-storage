#!/usr/bin/env python3
"""Module to insert a document into a MongoDB collection."""

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection based on keyword
    arguments.
 
    Parameters:
    mongo_collection: The pymongo collection object to insert into.
    **kwargs: Arbitrary keyword arguments representing the document
                fields and values.
    
    Returns:
    The _id of the inserted document.
    """
    # Insert the document using kwargs
    result = mongo_collection.insert_one(kwargs)
    
    # Return the _id of the inserted document
    return result.inserted_id

