from coutry_href import *



def get_cities(country_url, city1):
    """Получаем ссылку на город из переданной ссылки_страны и названия города"""
    resp = requests.get(country_url)
    html = resp.text

    soup = BeautifulSoup(html, 'lxml')
    tags_cities = soup('a', 'link place-list__item-name i-bem')

    cities = {}
    for tag in tags_cities:

        url = re.findall(r'href=\"(/pogoda/\D+\?via=reg)\"', str(tag))
        href = f'https://yandex.by{"".join(url)}'

        city = str.lower(tag.text) 
        if city:
            cities[city] = href
    city_url = cities.get(city1)

    return city_url








   