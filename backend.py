import requests

API_KEY = "ceec1a1c996b01f24c4fd5e62a05e4db"

def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    number_values= 8 * forecast_days
    filtered_data = filtered_data[:number_values]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Pune", forecast_days=3, kind="Sky"))