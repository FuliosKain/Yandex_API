import requests
from PIL import Image
from scale import scale
from io import BytesIO


def find_the_place(coords):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {"apikey": "8013b162-6b42-4997-9691-77b7074026e0",
                       "geocode": coords,
                       "format": "json"}
    response = requests.get(geocoder_api_server, params=geocoder_params)
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    param = scale(toponym)
    toponym_longitude, toponym_lattitude = param[0].split()

    apikey = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"

    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join([str(param[1]), str(param[2])]),
        "apikey": apikey
    }

    map_api_server = "https://static-maps.yandex.ru/v1"
    response = requests.get(map_api_server, params=map_params)
    image = BytesIO(response.content)
    print(image)
    image = Image.open(image)
    return image


find_the_place(('39.605562 52.565400'))
