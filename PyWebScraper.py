import requests
import random
from bs4 import BeautifulSoup


def save_html(html, path):
    with open(path, 'wb') as f:
        # print(type(f.write(html)))
        return f.write(html)


def open_html(path):
    with open(path, 'rb') as f:
        return f.read()


def make_requests(url, user=True):
    if user:
        return requests.get(url, headers={'User-Agent': random.choice(users)})
    return requests.get(url)




users = [
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36']


song_list_url = 'https://www.azlyrics.com/l/lonelyisland.html'
general_url = 'https://www.azlyrics.com'

pre_soup_songs = make_requests(song_list_url)

save_html(pre_soup_songs.content, 'songsPages')

html = open_html('songsPages')

allSongsSoup = BeautifulSoup(html, 'html.parser')

songs_list = allSongsSoup.select('a[href*=lonelyisland]')

for i in range(len(songs_list)):
    link = (songs_list[i]).get('href')
    song_url = general_url + link[2:]
    print(song_url)


# print(len(songs_list))
