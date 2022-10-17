import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
import urllib
import sip

def is_valid(url):
    """
    Проверяет, является ли url допустимым URL
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_images(url):
    """
    Возвращает все URL‑адреса изображений по одному `url`
    """
    soup = bs(requests.get(url).content, "html5lib")
    print(soup)
    urls = []
    print(soup.find_all('div'))
    for img in tqdm(soup.find_all("img"), "Extracting images"):
        img_url = img.attrs.get("src")
        print(img_url)
        print(soup)
        if not img_url:
            # если img не содержит атрибута src, просто пропустите
            continue
        img_url = urljoin(url, img_url)
        try:
            pos = img_url.index("?")
            img_url = img_url[:pos]
        except ValueError:
            pass
        if is_valid(img_url):
            urls.append(img_url)
    return urls
url = 'https://knowyourmeme.com/photos/2306860-things-that-look-like-among-us-crewmates'
print(is_valid(url))
print(get_all_images(url))
print(urllib.request.urlopen(url))
print(requests.get(url).status_code)