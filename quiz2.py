from pymongo import MongoClient

client = MongoClient('mongodb+srv://user:sparta@cluster0.uwkgh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

db = client.dbsparta

# target_movie = db.movies.find_one({'movie': '3. The Dark Knight'})
# target_rating = target_movie['rating']

# movies = list(db.movies.find({'rating': target_rating}))

# for movie in movies:
#     print(movie['movie'])

db.movies.update_one(
    {'movie': '3. The Dark Knight'},
    {'$set': {'rating': 0}}
)

movie = db.movies.find_one({'movie':'3. The Dark Knight'})
print(movie)