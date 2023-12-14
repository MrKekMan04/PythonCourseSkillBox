import json

import requests
from requests import Response


def get_page(path: str) -> Response:
    return requests.get(url=path)


def get_world_name(path: str) -> str:
    response = get_page(path)

    if response.status_code == 200:
        return dict(json.loads(response.text))["name"]


def get_pilot_info(path: str) -> dict:
    response = get_page(path)

    if response.status_code == 200:
        pilot_data = dict(json.loads(response.text))

        return {
            "name": pilot_data["name"],
            "height": pilot_data["height"],
            "mass": pilot_data["mass"],
            "homeworld": get_world_name(pilot_data["homeworld"]),
            "homeworld_url": pilot_data["homeworld"]
        }


def get_millennium_falcon_info() -> dict:
    response = get_page("https://swapi.dev/api/starships/10")

    if response.status_code == 200:
        ship_data = dict(json.loads(response.text))

        return {
            "max_atmosphering_speed": ship_data["max_atmosphering_speed"],
            "pilots": [get_pilot_info(pilot_api_page) for pilot_api_page in ship_data["pilots"]],
            "ship_name": ship_data["name"],
            "starship_class": ship_data["starship_class"]
        }


def main():
    info = get_millennium_falcon_info()

    print(info)

    with open("ship_data.json", "w", encoding="UTF-8") as file:
        json.dump(info, file, indent=4)


if __name__ == '__main__':
    main()
