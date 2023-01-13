import requests

cities = ("Хабаровск", "Уфа", "Нижний+Новгород", "Калининград")

responses = []
for city in cities:
    apikey = "40d1649f-0493-4b70-98ba-98533de7710b"
    geocoder_request = (
        f"https://geocode-maps.yandex.ru/1.x/?apikey={apikey}&geocode={city}&format=json"
    )
    responses.append(requests.get(geocoder_request))

for response in responses:
    if response:
        json_response = response.json()

        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        toponym_city = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][-1][
            "name"
        ]
        toponym_area = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][1][
            "name"
        ]
        print(f"{toponym_city}: {toponym_area}")
    else:
        print("Ошибка выполнения запроса:")
        print(geocoder_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
