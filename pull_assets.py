import requests
import json

def pull_assets():
    url = "https://securitytapestry.freshservice.com/api/v2/assets?filter=\"department_id:21000185204\"&include=type_fields"
    request = requests.get(url, auth=('p4CWhwgKyWmyrJrKWJ','X'))
    response = request.json()["assets"]
    for asset in response:
        save_asset_json(asset)
    # print(response)
    # save_asset_json(response)

def save_asset_json(data):
    with open(f"docs/assets/asset-{str(data['display_id'])}.json","w",encoding="UTF-8") as asset:
        json.dump(data, asset, indent=4)

if __name__ == "__main__":
    pull_assets()