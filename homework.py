from pymongo import MongoClient

client = MongoClient('mongodb+srv://user:sparta@cluster0.uwkgh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

db = client.dbsparta

# db.books.insert_one({
#     'title' : 'Harry Potter',
#     'author': 'Rowling',
#     'rating': 90
# })
# db.books.insert_one({
#     'title' : 'The Fisherman and the Fish',
#     'author' : 'Joseph Choi',
#     'rating' : 10
# })
# db.books.insert_one({
#     'title' : 'Fire in the Water',
#     'author' : 'Some Dude',
#     'rating' : 57
# })

# db.books.update_one(
#     {'title':'The Fisherman and the Fish'},
#     {'$set':{'author': 'Jimmy Kim'}}
# )

db.books.delete_one({'rating' : 90})

all_users = list(db.books.find({},{'_id':False}))

for user in all_users:
    print(user)

