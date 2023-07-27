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

DEPARTMENT_ID = "21000376117"


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
    remove_keys_primary = [
        'description','impact','usage_type',
        'asset_tag','user_id','location_id',
        'agent_id','group_id','assigned_on',
        'created_at','updated_at','end_of_life',
        'discovery_enabled','author_type','asset_type_id',
        'department_id'
        ]
    remove_keys_secondary = [
        'vendor_21001393125',
        'cost_21001393125',
        'warranty_21001393125',
        'acquisition_date_21001393125',
        'warranty_expiry_date_21001393125',
        'depreciation_id',
        'salvage'
    ]
    iterator = 0
    for asset in json_input:
        if asset['author_type'] != 'Discovery Agent':
            json_input.pop(iterator)
        iterator += 1
    for asset in json_input:
        for key in remove_keys_primary:
            del asset[key]
        for key in remove_keys_secondary:
            del asset['type_fields'][key]

    return json_input


if __name__ == '__main__':
    pull_assets()
