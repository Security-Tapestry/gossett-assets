from dotenv import load_dotenv
import requests
import json
import os

if not os.getenv("FS_API"):
    load_dotenv()

def pull_assets():
    url = "https://securitytapestry.freshservice.com/api/v2/assets?filter=\"department_id:21000185204\"&include=type_fields"
    request = requests.get(url, auth=(os.getenv("FS_API"),'X'))
    response = request.json()["assets"]
    save_asset_json(response)

def save_asset_json(data):
    with open("docs/assets.json","w",encoding="UTF-8") as assets:
        json.dump(data, assets, indent=4)

if __name__ == "__main__":
    pull_assets()