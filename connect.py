from pymongo import MongoClient

client = MongoClient('mongodb+srv://user:sparta@cluster0.uwkgh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

db = client.dbsparta

doc = {
    'name':'bob',
    'age':27
}

db.users.insert_one(doc)