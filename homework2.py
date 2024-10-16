import requests
from bs4 import BeautifulSoup

# Baca URLnya dan ambil HTMLnya,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

# Kamu akan memulai "scraping" dari data pada halaman ini
url = 'https://www.billboard.com/charts/hot-100'

# Gunakan requests library untuk mendapatkan kode HTML dari link diatas
data = requests.get(url=url, headers=headers)

# library BeautifulSoup memudahkan kita dalam
# menguraikan kode HTML tersebut,
soup = BeautifulSoup(data.text, 'html.parser')

# Menggunakan select
songs = soup.select('.o-chart-results-list-row')

# Looping pada setiap lagunya
for song in songs:
    # Pertama, ambil rank lagu
    rank = song.select_one('.o-chart-results-list__item > span').text.strip()
    # Ambil judul lagu
    title_song = song.select_one('.o-chart-results-list__item > h3').text.strip()
    # Ambil penyayi lagu
    artis = song.parent.select_one('.a-font-primary-s').text.strip()
    
    print(rank,'/', title_song, '/', artis)