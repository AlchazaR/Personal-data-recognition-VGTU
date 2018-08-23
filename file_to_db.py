import pymongo
from pymongo import MongoClient
import datetime

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
            col.update(fileToChange, newData)
            return(col.find({'filePath':fPath}))
    else:
        # if document not exists, insert it
        col.insert_one({
            'filePath':fPath, 
            'fileHash':fHash, 
            'scanDate':None})
        return(col.find({'filePath':fPath}))


if __name__ == '__main__':
    print(add_file_to_db('/home/vlad/Documents/Repo/python_string-search/text_sources/test-list.txt', 'ajdhakfhkshfdjkh11'))
    