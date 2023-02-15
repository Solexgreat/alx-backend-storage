#!/usr/bin/env python3
"""10 update"""


def update_topics(mongo_collection, name, topics):
    """ function update with arg name to topics"""
    result = mongo_collection.updateMany({
        "name" : name},
        {"$set": {"topics": topics}})  