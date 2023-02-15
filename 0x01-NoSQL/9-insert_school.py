#!/usr/bin/env python3
"""9 insert with py"""


def insert_document(mongo_collection, **kwargs):
    """Function takes number of keyword and insert 
        to our collection"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id