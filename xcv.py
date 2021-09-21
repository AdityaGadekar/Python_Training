from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
myclient = MongoClient("mongodb://%s:%s@127.0.0.1" %('myUserAdmin', 'abc123'))
print("connection successful", myclient)

# list down the databases
list_of_db = myclient.list_database_names()
print("databases available in mongodb", list_of_db)



# create new database in mongodb
mydb = myclient['test']
print("Database created...", mydb)
collection = mydb['student']
curson = collection.find({"marks":{"$gt":45}})
print("The records greater than 45")
for record in curson:
    print("records:%s" % record)
"""
cursor = collection.find({"marks":{"$lt":45}})
print("The records less than 45")
for record in cursor:
    print("records:%s" % record)