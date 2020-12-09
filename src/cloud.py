import requests

def get_current_data():
    result = requests.get(
        url='http://localhost:3000/sensorsData'
    ).json()

    return result


def get_current_temperature():
    result = requests.get(
        url='http://localhost:3000/temperatureData'
    ).json()

    return result


def get_current_humidity_air():
    result = requests.get(
        url='http://localhost:3000/humidityAirData'
    ).json()

    return result


def get_current_brightness_level():
    result = requests.get(
        url='http://localhost:3000/brightnessLevelData'
    ).json()

    return result


def set_temperature(value):
    requests.post(
    url='http://localhost:3000/temperatureData',
    json={
        "temperature": str(value),
    })


def set_humidity_air(value):
    requests.post(
    url='http://localhost:3000/humidityAirData',
    json={
        "humidityAir": str(value),
    })


def set__brightness_level(value):
    requests.post(
    url='http://localhost:3000/brightnessLevelData',
    json={
        "brightnessLevel": str(value),
    })
