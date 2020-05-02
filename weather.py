from coutry_href import *
from city_href import *

def get_weather(city_url):
    resp = requests.get(city_url)
    html = resp.text

    soup = BeautifulSoup(html, 'lxml')

    temp = soup.find_all('span', 'temp__value')
    current_temp = temp[1].text
    feels_like = temp[2].text
    clouds = soup.find('div', 'link__condition day-anchor i-bem').text

    rainfall = soup.find('p', 'maps-widget-fact__title').text

    weather = [current_temp, feels_like, clouds, rainfall]
    return weather
