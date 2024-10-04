import requests
from bs4 import BeautifulSoup

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
    print(movie_title, '/', year, '/', rating)

# selector  
    #__next > main > div > div.ipc-page-content-container.ipc-page-content-container--center > section > div > div.ipc-page-grid.ipc-page-grid--bias-left > div > ul
    #__next > main > div > div.ipc-page-content-container.ipc-page-content-container--center > section > div > div.ipc-page-grid.ipc-page-grid--bias-left > div > ul > li:nth-child(1) > div.ipc-metadata-list-summary-item__c > div > div > div.ipc-title.ipc-title--base.ipc-title--title.ipc-title-link-no-icon.ipc-title--on-textPrimary.sc-ab348ad5-9.cIVpMc.cli-title > a > h3
    #__next > main > div > div.ipc-page-content-container.ipc-page-content-container--center > section > div > div.ipc-page-grid.ipc-page-grid--bias-left > div > ul > li:nth-child(2) > div.ipc-metadata-list-summary-item__c > div > div > div.sc-ab348ad5-7.cqgETV.cli-title-metadata > span:nth-child(1)
    #__next > main > div > div.ipc-page-content-container.ipc-page-content-container--center > section > div > div.ipc-page-grid.ipc-page-grid--bias-left > div > ul > li:nth-child(2) > div.ipc-metadata-list-summary-item__c > div > div > span > div > span > span.ipc-rating-star--rating