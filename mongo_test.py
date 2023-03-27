from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")


mydatabase = client['test']
z = mydatabase['test'].find()

for b in z:
    print(b)
                     


