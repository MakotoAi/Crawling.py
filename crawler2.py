import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient           # Importing pymongo (You have to install the package first)

client = MongoClient('mongodb+srv://user:sparta@cluster0.uwkgh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')  # mongoDB goes back to port 27017.
db = client.dbsparta                      # Create a db named 'dbsparta'.

# Baca URLnya dan ambil HTMLnya,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

# Kamu akan memulai "scraping" dari data pada halaman ini
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

# Gunakan requests library untuk mendapatkan kode HTML dari link diatas
data = requests.get(url=url, headers=headers)

# library BeautifulSoup memudahkan kita dalam
# menguraikan kode HTML tersebut,
soup = BeautifulSoup(data.text, 'html.parser')

# Menggunakan select
movies = soup.select('.ipc-page-grid > div > ul > li')

# Looping pada setiap filmnya
for movie in movies:
    # Pertama, ambil judul dari filmnya
    movie_title = movie.select_one('.ipc-title > a').text
    # Ambil tahun filmnya
    year = movie.select_one('.sc-ab348ad5-7 > span').text
    # Ambil rating filmnya
    rating = movie.select_one('.ipc-rating-star--rating').text
    
    doc = {
        'movie' : movie_title,
        'year' : year,
        'rating' : rating
    }
    db.movies.insert_one(doc)