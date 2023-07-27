#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Module for pulling assets and creating views"""

import os
import json
from dotenv import load_dotenv
import requests

if not os.getenv("FS_API"):
    load_dotenv()


def pull_assets():
    url = 'https://securitytapestry.freshservice.com/api/v2/assets?filter="department_id:21000185204"&include=type_fields'
    request = requests.get(url, auth=(os.getenv('FS_API'), 'X'), timeout=30)
    response = request.json()['assets']
    save_asset_json(response)


def save_asset_json(data):
    with open('docs/assets.json', 'w', encoding='UTF-8') as assets:
        json.dump(data, assets, indent=4)


def create_html():
    pass


if __name__ == '__main__':
    pull_assets()
