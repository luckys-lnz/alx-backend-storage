#!/usr/bin/env python3
"""Module to list all documents in a MongoDB collection."""

def list_all(mongo_collection):
    """List all documents in a given collection.
    
    Args:
        mongo_collection (pymongo.collection.Collection): The collection to search.

    Returns:
        list: A list of documents found in the collection, or an empty list if no documents found.
    """
    documents = list(mongo_collection.find())
    return documents if documents else []

