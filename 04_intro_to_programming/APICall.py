#! /usr/bin/python3


def location (lat, long, SECRET_KEY):
    import requests
    
    response = requests.get('https://api.darksky.net/forecast/{key}/{lat},{long}'.format(
        key=SECRET_KEY, lat=lat, long=long))
    data = response.json()
    print(data)

location('41.0037', '80.2470','1d8c58ed1d54f96f939e706c788650f1' )