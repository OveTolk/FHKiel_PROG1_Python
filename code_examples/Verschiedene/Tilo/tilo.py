import requests

def get_puuid(name, tag):
    api_key = "c4ccf31f89d1ca766bf044ae2877155d"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={name}&lon={tag}&appid={api_key}"
    
    headers = {
        "X-Riot-Token": api_key
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        ort = data["name"]
        land = data["sys"]["country"]
        wetterzustand = data["weather"][0]["main"]
        ausgabe = f"An den Koordinaten befindet sich der Ort {ort} im Land {land} und es ist {wetterzustand}"
        return ausgabe
    else:
        print("Error:", response.status_code, response.text)

def get_userinfo():
    x = input("Lat: ")
    y = input("Lon: ")
    return x, y

def main():
    name, tag = get_userinfo()
    puuid = get_puuid(name, tag)
    print(puuid)

main()