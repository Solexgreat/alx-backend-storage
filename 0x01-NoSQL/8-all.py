#!/usr/bin/env python3
"""REturn the list of all document"""
import pymongo 


def list_all(mongo_collection):
    """Function recieves collection, loop and 
        and append the document to a list"""

    documents = mongo_collection.find()    
    doc_list = []

    if documents.count == 0:
        return(doc_list)

    for document in documents:
        doc_list.append(document)
    print(doc_list)
