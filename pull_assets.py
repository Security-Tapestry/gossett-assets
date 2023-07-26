import requests
import json

def pull_assets():
    # asset_filter = "department_id:21000185204"
    url = "https://securitytapestry.freshservice.com/api/v2/assets?filter=\"department_id:21000185204\""
    request = requests.get(url, auth=('p4CWhwgKyWmyrJrKWJ','X'))
    response = request.json()["assets"]
    print(response)
    with open("docs/assets.json","w",encoding="UTF-8") as assets:
        json.dump(response, assets, indent=4)

if __name__ == "__main__":
    pull_assets()