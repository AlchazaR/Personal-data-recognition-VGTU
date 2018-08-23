import pymongo
from pymongo import MongoClient
import datetime

"""
    Add found file and it hash to Database
"""
def add_file_to_db(fPath, fHash):
    client = MongoClient('localhost', 27017)
    db = client.files_list
    col = db.files_data
    # find document
    if col.find({'filePath':fPath}).count() > 0:
        # if document exists
        if col.find({'fileHash':fHash, 'filePath':fPath}).count() < 1:
            # if hash different, update scanDate to None
            fileToChange = {'filePath':fPath}
            newData = {"$set":{
                'fileHash':fHash, 
                'scanDate':None}}
            col.update_one(fileToChange, newData)
            return(True)
        else:
            return(False)
    else:
        # if document not exists, insert it
        col.insert_one({
            'filePath':fPath, 
            'fileHash':fHash, 
            'scanDate':None})
        return(True)

"""
    Add found Names/Surnames to database
"""
def add_names(fPath, names):
    client = MongoClient('localhost', 27017)
    db = client.files_list
    col = db.files_data
    # find document
    if col.find({'filePath':fPath}).count() > 0:
        fileToChange = {'filePath':fPath}
        newData = {"$push":{
            'foundNames':names}}
        col.update_one(fileToChange, newData)

"""
    Set date of last file scan
"""
def set_date(fPath):
    client = MongoClient('localhost', 27017)
    db = client.files_list
    col = db.files_data
    # find document
    if col.find({'filePath':fPath}).count() > 0:
        fileToChange = {'filePath':fPath}
        newDate = {"$set":{
            'scanDate':datetime.datetime.now}}
        col.update_one(fileToChange, newDate)   

if __name__ == '__main__':
    print(add_file_to_db('/home/vlad/Documents/Repo/python_string-search/text_sources/test-list.txt', 'ajdhakfhkshfdjkh11'))
    