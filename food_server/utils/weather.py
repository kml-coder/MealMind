def get_weather(lat, lon):
    url = f"http://api.weatherapi.com/v1/current.json?key=e1f05821ef414dc6bef31818252603&q={lat},{lon}&lang=kr"
    res = requests.get(url).json()
    return {
        "condition": res["current"]["condition"]["text"],
        "temp_c": res["current"]["temp_c"]
    }
