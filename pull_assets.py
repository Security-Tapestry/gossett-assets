import requests
import json

def pull_assets():
    url = "https://securitytapestry.freshservice.com/api/v2/assets?filter=\"department_id:21000185204\""
    request = requests.get(url, auth=('p4CWhwgKyWmyrJrKWJ','X'))
    response = request.json()["assets"]
    for asset in response:
        get_asset_details(asset)
    # print(response)
    # save_asset_json(response)

def get_asset_details(asset):
    url = "https://securitytapestry.freshservice.com/api/v2/assets/" + str(asset["display_id"]) + "?include=type_fields"
    request = requests.get(url, auth=('p4CWhwgKyWmyrJrKWJ','X'))
    response = request.json()["asset"]
    save_asset_json(response)

def save_asset_json(data):
    display_id = str(data["display_id"])
    with open(f"docs/assets/asset-{display_id}.json","w",encoding="UTF-8") as asset:
        json.dump(data, asset, indent=4)

if __name__ == "__main__":
    pull_assets()