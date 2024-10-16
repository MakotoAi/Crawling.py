from pymongo import MongoClient

client = MongoClient('mongodb+srv://user:sparta@cluster0.uwkgh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
# client = MongoClient('mongodb+srv://user:sparta@cluster0.uwkgh.mongodb.net/')

db = client.dbsparta

# doc1 = {'name':'Alim','age':22 }
# doc2 = {'name':'kay','age':27 }
# doc3 = {'name':'john','age':30 }

# db.users.insert_one(doc1)
# db.users.insert_one(doc2)
# db.users.insert_one(doc3)

# all_users = list(db.users.find({},{'_id':False}))

# Lihat semua data di MongoDB
all_users = list(db.users.find({},{'_id':False}))

print(all_users[0])         # Memperlihatkan hasil 0
# print(all_users[0]['name']) # Memperlihatkan 'nama' dari hasil 0

# for user in all_users:      # loop through serta lihat seluruh hasilnya
    # print(user)

#  db.users.update_one({'name':'bobby'},{'$set':{'age':19  }})

# user = db.users.find_one({'name':'bobby'})
# print(user)

# db.users.delete_one({'name':'bobby'})

# user = db.users.find_one({'name':'bobby'})
# print(user)