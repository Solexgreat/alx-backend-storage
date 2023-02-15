#!/urs/bin/env python3
"""REturn the list of all document"""


from pymongo import MongoClient


def list_all(mongo_collection):
    """Function recieves collection, loop and 
        and append the document to a list"""
    doc_list = []

    if len(mongo_collection) == 0:
        return(doc_list)

    for document in mongo_collection:
        doc_list.append(document)
        print(doc_list)
