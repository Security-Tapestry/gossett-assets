#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Module for pulling assets and creating views"""

import os
import json
from dotenv import load_dotenv
from json2html import * # pylint: disable=W0401,W0614
import requests

if not os.getenv("FS_API"):
    load_dotenv()

DEPARTMENT_ID = "21000185204"


def pull_assets():
    """Pull Assets from FreshService API"""
    url = 'https://securitytapestry.freshservice.com/api/v2/assets' + (
        f'?filter="department_id:{DEPARTMENT_ID}"&include=type_fields' )
    request = requests.get(url, auth=(os.getenv('FS_API'), 'X'), timeout=30)
    response = request.json()['assets']
    save_asset_json(clean_json(response))
    create_html(json.load(open('docs/assets.json', 'r', encoding='UTF-8')))


def save_asset_json(data):
    """Save JSON to file"""
    with open('docs/assets.json', 'w', encoding='UTF-8') as assets:
        json.dump(data, assets, indent=4)


def create_html(json_input):
    """Create HTML from JSON data"""
    html_string = json2html.convert(json_input, 'id="assets" class="table table-bordered"')
    with open('docs/index.html','w',encoding='UTF-8') as html:
        html.write(
            '<!DOCTYPE html>\n'
            + '<html>\n<head>\n'
            + '<link rel="stylesheet" href="style.css">\n</head>\n<body>\n'
            + html_string
            + '\n</body>\n</html>')


def clean_json(json_input):
    """Remove unnecessary keys from JSON"""
    iterator = 0
    for asset in json_input:
        if asset['author_type'] != 'Discovery Agent':
            json_input.pop(iterator)
        iterator += 1
    for asset in json_input:
        del asset['description']
        del asset['impact']
        del asset['usage_type']
        del asset['asset_tag']
        del asset['user_id']
        del asset['location_id']
        del asset['agent_id']
        del asset['group_id']
        del asset['assigned_on']
        del asset['created_at']
        del asset['updated_at']
        del asset['end_of_life']
        del asset['discovery_enabled']
        del asset['author_type']
        del asset['asset_type_id']
        del asset['department_id']

    return json_input


if __name__ == '__main__':
    pull_assets()
