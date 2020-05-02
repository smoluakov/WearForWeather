import requests
from bs4 import BeautifulSoup
import re



def get_countries(country1):
    resp = requests.get("https://yandex.by/pogoda/region?via=brd")
    html = resp.text

    soup = BeautifulSoup(html, 'lxml')
    
    tags_countries = soup.find_all('a', 'link place-list__item-name i-bem')

    countries = {}
    for tag in tags_countries:

        url = re.findall(r'href=\"(/pogoda/region/\d+[?]via=reg)\"', str(tag))
        href = f'https://yandex.by{"".join(url)}'

        country = str.lower(tag.text) 
        if country:
            countries[country] = href
    country_url = countries.get(country1)
    return country_url


