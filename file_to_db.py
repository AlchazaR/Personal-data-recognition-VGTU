import pymongo
from pymongo import MongoClient
import datetime

"""
    Database info:
        Connect to mongo DB: mongo
        Show databases: show dbs
        Select database: use files_list
        Drop Collection: db.files_data.drop()
        Create index: db.files_data.ensureIndex({foundNames:'text'})
        Search for text: db.files_data.find({$text:{$search:'Marija'}})
        show all data: db.files_data.find().pretty()
    
    DB structure:
        "_id" : ObjectId("5b804f27e9ac19216e7364a7"),
        "scanDate" : null,
	    "filePath" : "/home/vlad/Documents/Repo/python_string-search/text_sources/wiki-straipsnis.txt",
	    "fileHash" : "570700d955264296eed2bb905b65128e",
	    "foundNames" : ["Name", "Name2"]

"""


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
        print('Documents already exists in DB')
        if col.find({'fileHash':fHash, 'filePath':fPath}).count() < 1:
            # if hash different, update scanDate to None
            print('Document edited, it will be scanned for personal data')
            fileToChange = {'filePath':fPath}
            newData = {"$set":{
                'fileHash':fHash, 
                'scanDate':None,
                'foundNames':''}}
            col.update_one(fileToChange, newData)
            return(True)
        else:
            return(False)
    else:
        # if document not exists, insert it
        print('New document')
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
        names = names.strip('[]"')
        names = names.replace(',', ';')
        #print(names)
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
    