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

DEPARTMENT_ID = 21000376117

COMPANY_NAME = "Gossett Motors"

REQUEST_URL = (
    'https://securitytapestry.freshservice.com/api/v2/assets') + (
    f'?include=type_fields&filter="department_id:{str(DEPARTMENT_ID)}"'
)


def pull_assets():
    """Pull Assets from FreshService API"""
    (
        page_1, page_2, page_3, page_4,
        page_5, page_6, page_7, page_8,
        page_9, page_10, page_11, page_12,
        page_13, page_14, page_15
    ) = (
        pull_assets_page_1(), pull_assets_page_2(),
        pull_assets_page_3(), pull_assets_page_4(),
        pull_assets_page_5(), pull_assets_page_6(),
        pull_assets_page_7(), pull_assets_page_8(),
        pull_assets_page_9(), pull_assets_page_10(),
        pull_assets_page_11(), pull_assets_page_12(),
        pull_assets_page_13(), pull_assets_page_14(),
        pull_assets_page_15()
    )
    combined_json = (
        page_1 + page_2 + page_3 + page_4 ) + (
        page_5 + page_6 + page_7 + page_8 ) + (
        page_9 + page_10 + page_11 + page_12 ) + (
        page_13 + page_14 + page_15
    )
    save_asset_json(clean_json(combined_json))
    with open('docs/assets.json', 'r', encoding='UTF-8') as file:
        create_html(json.load(file))


def pull_assets_page_1():
    """Pull Assets from FreshService API"""
    url = REQUEST_URL
    request = requests.get(url, auth=(os.getenv('FS_API'), 'X'), timeout=30)
    response= request.json()['assets']

    return response


def pull_assets_page_2():
    """Pull Assets from FreshService API"""
    url = REQUEST_URL + '&page=2'
    request = requests.get(url, auth=(os.getenv('FS_API'), 'X'), timeout=30)
    response= request.json()['assets']

    return response


def pull_assets_page_3():
    """Pull Assets from FreshService API"""
    url = REQUEST_URL + '&page=3'
    request = requests.get(url, auth=(os.getenv('FS_API'), 'X'), timeout=30)
    response= request.json()['assets']

    return response


def pull_assets_page_4():
    """Pull Assets from FreshService API"""
    url = REQUEST_URL + '&page=4'
    request = requests.get(url, auth=(os.getenv('FS_API'), 'X'), timeout=30)
    response= request.json()['assets']

    return response


def pull_assets_page_5():
    """Pull Assets from FreshService API"""
    url = REQUEST_URL + '&page=5'
    request = requests.get(url, auth=(os.getenv('FS_API'), 'X'), timeout=30)
    response= request.json()['assets']

    return response


def pull_assets_page_6():
    """Pull Assets from FreshService API"""
    url = REQUEST_URL + '&page=6'
    request = requests.get(url, auth=(os.getenv('FS_API'), 'X'), timeout=30)
    response= request.json()['assets']

    return response


def pull_assets_page_7():
    """Pull Assets from FreshService API"""
    url = REQUEST_URL + '&page=7'
    request = requests.get(url, auth=(os.getenv('FS_API'), 'X'), timeout=30)
    response= request.json()['assets']

    return response


def pull_assets_page_8():
    """Pull Assets from FreshService API"""
    url = REQUEST_URL + '&page=8'
    request = requests.get(url, auth=(os.getenv('FS_API'), 'X'), timeout=30)
    response= request.json()['assets']

    return response


def pull_assets_page_9():
    """Pull Assets from FreshService API"""
    url = REQUEST_URL + '&page=9'
    request = requests.get(url, auth=(os.getenv('FS_API'), 'X'), timeout=30)
    response= request.json()['assets']

    return response


def pull_assets_page_10():
    """Pull Assets from FreshService API"""
    url = REQUEST_URL + '&page=10'
    request = requests.get(url, auth=(os.getenv('FS_API'), 'X'), timeout=30)
    response= request.json()['assets']

    return response


def pull_assets_page_11():
    """Pull Assets from FreshService API"""
    url = REQUEST_URL + '&page=11'
    request = requests.get(url, auth=(os.getenv('FS_API'), 'X'), timeout=30)
    response= request.json()['assets']

    return response


def pull_assets_page_12():
    """Pull Assets from FreshService API"""
    url = REQUEST_URL + '&page=12'
    request = requests.get(url, auth=(os.getenv('FS_API'), 'X'), timeout=30)
    response= request.json()['assets']

    return response


def pull_assets_page_13():
    """Pull Assets from FreshService API"""
    url = REQUEST_URL + '&page=13'
    request = requests.get(url, auth=(os.getenv('FS_API'), 'X'), timeout=30)
    response= request.json()['assets']

    return response


def pull_assets_page_14():
    """Pull Assets from FreshService API"""
    url = REQUEST_URL + '&page=14'
    request = requests.get(url, auth=(os.getenv('FS_API'), 'X'), timeout=30)
    response= request.json()['assets']

    return response


def pull_assets_page_15():
    """Pull Assets from FreshService API"""
    url = REQUEST_URL + '&page=15'
    request = requests.get(url, auth=(os.getenv('FS_API'), 'X'), timeout=30)
    response= request.json()['assets']

    return response


def save_asset_json(data):
    """Save JSON to file"""
    with open('docs/assets.json', 'w', encoding='UTF-8') as assets:
        json.dump(data, assets, indent=4)


def create_html(json_input):
    """Create HTML from JSON data"""
    html_string = json2html.convert(json_input, 'id="assets" class="dataframe sortable"')
    with open('docs/index.html','w',encoding='UTF-8') as html:
        html.write(
            '<!DOCTYPE html>\n'
            + '<html>\n<head>\n'
            + f'<title>{COMPANY_NAME} Assets</title>\n'
            + '<link rel="stylesheet" href="assets/dataframe.css">\n'
            + '<link rel="stylesheet" href="assets/filtertable.css">\n'
            + '<script src="assets/sorttable.js"></script>\n'
            + '</head>\n<body>\n'
            + '<script src="assets/key.js"></script>\n'
            + f'<a id="assetCount">Assets: {len(json_input)}</a><br><br>\n'
            + '<input type="text" id="hostnameSearch" onkeyup="filterHostname()" placeholder="Hostname...">\n' # pylint: disable=C0301
            + '&nbsp;'
            + '<input type="text" id="serialSearch" onkeyup="filterSerial()" placeholder="Serial/Asset Tag...">\n' # pylint: disable=C0301
            + '&nbsp;'
            + '<input type="text" id="macSearch" onkeyup="filterMAC()" placeholder="MAC Address...">\n' # pylint: disable=C0301
            + '&nbsp;'
            + '<input type="text" id="ipSearch" onkeyup="filterIP()" placeholder="IP Address...">\n' # pylint: disable=C0301
            + '&nbsp;'
            + '<input type="text" id="productSearch" onkeyup="filterProduct()" placeholder="Product...">\n' # pylint: disable=C0301
            + html_string
            + '\n</body>\n<script src="assets/filtertable.js"></script>\n'
            + '</html>')


def clean_json(json_input):
    """Remove unnecessary items from JSON and renaming keys"""
    iterator = 0
    remove_keys_primary = [
        'description','impact','usage_type','asset_tag','user_id','location_id',
        'agent_id','group_id','assigned_on','created_at','updated_at','end_of_life',
        'discovery_enabled','author_type','asset_type_id','department_id','display_id','id'
    ]
    remove_keys_secondary = [
        'vendor_21001393125','cost_21001393125','warranty_21001393125',
        'acquisition_date_21001393125','warranty_expiry_date_21001393125',
        'depreciation_id','salvage'
    ]
    rename_keys = {
        'domain_21001393125': 'Domain',
        'asset_state_21001393125': 'State',
        'serial_number_21001393125': 'Serial_Number',
        'os_21001393130': 'OS',
        'os_version_21001393130': 'Version',
        'os_service_pack_21001393130': 'Service_Pack',
        'memory_21001393130': 'Memory_GB',
        'disk_space_21001393130': 'Disk_Space_GB',
        'cpu_speed_21001393130': 'CPU_Speed_GHz',
        'cpu_core_count_21001393130': 'CPU_Core_Count',
        'mac_address_21001393130': 'MAC_Address',
        'uuid_21001393130': 'UUID',
        'hostname_21001393130': 'Hostname',
        'computer_ip_address_21001393130': 'IP_Address',
        'last_login_by_21001393130': 'Last_Logged_in_User',
        'last_audit_date_21001393125': 'Last_Check_In',
        'product_21001393125': 'Product',
    }
    attributes = [
        'Domain', 'State', 'Serial_Number', 'OS', 'Version',
        'Service_Pack', 'Memory_GB', 'Disk_Space_GB', 'CPU_Speed_GHz',
        'CPU_Core_Count', 'MAC_Address', 'UUID', 'Hostname',
        'IP_Address', 'Last_Logged_in_User', 'Last_Check_In', 'Product'
    ]
    product_and_vendors = {
        21000221593: 'Acer VZ4820G', 21000221577: 'Acer Veriton X4640G',
        21000221574: 'Acer Veriton M2611G', 21000221566: 'Acer Veriton M2632G',
        21000221589: 'Acer Veriton M4618G', 21000221587: 'Acer Veriton M4640G',
        21000221573: 'Acer Veriton M4650G', 21000221588: 'Dell Latitude 3500',
        21000221564: 'Dell OptiPlex 3000', 21000221590: 'Dell OptiPlex 3010',
        21000221592: 'Dell OptiPlex 3040', 21000221549: 'Dell OptiPlex 3050',
        21000221446: 'Dell OptiPlex 3060', 21000221571: 'Dell OptiPlex 3070',
        21000221570: 'Dell OptiPlex 3080', 21000221550: 'Dell OptiPlex 5060',
        21000221597: 'Dell OptiPlex 960', 21000221563: 'Dell OptiPlex SFF 7010',
        21000221586: 'Dell Precision 3630 Tower', 21000221591: 'Dell Precision T3610',
        21000224159: 'Dell PowerEdge R740', 21000221576: 'GETAC S410',
        21000221600: 'GETAC S410G3', 21000221578: 'GETAC S410G4',
        21000221565: 'HP EliteBook 840 G2', 21000221569: 'HP ProBook 4540s',
        21000224162: 'HPE ProLiant DL160 G6', 21000224161: 'HPE ProLiant DL380 Gen10',
        21000224163: 'HPE ProLiant DL560 Gen10', 21000221601: 'LENOVO ThinkBook 15 G2 ARE',
        21000221572: 'LENOVO ThinkBook 15 G2 ITL', 21000221575: 'LENOVO ThinkPad E14',
        21000221599: 'LENOVO ThinkPad E14 Gen 2', 21000221602: 'LENOVO ThinkPad E580',
        21000221595: 'LENOVO ThinkPad Edge E440', 21000221568: 'LENOVO ThinkPad Edge E531',
        21000221567: 'LENOVO ThinkPad L15 Gen 1', 21000224164: 'LENOVO ThinkPad T440p',
        21000224160: 'Microsoft Hyper-V Virtual Machine', 21000221562: 'Panasonic CF-52JE2VWVW',
        21000221594: 'Panasonic CF-54-1', 21000221596: 'Panasonic FZ55-1'
    }

    for asset in json_input:
        if asset['author_type'] == 'User':
            json_input.pop(iterator)
        iterator += 1

    for asset in json_input:
        for key in remove_keys_primary:
            asset.pop(key)
        for key in remove_keys_secondary:
            try:
                asset['type_fields'].pop(key)
            except KeyError:
                continue
        for key,value in rename_keys.items():
            try:
                asset['type_fields'][value] = asset['type_fields'].pop(key)
            except KeyError:
                continue

    for asset in json_input:
        
        for product_id, value in product_and_vendors.items():
            if asset['type_fields']['Product'] == product_id:
                asset['type_fields']['Product'] = value

    for asset in json_input:
        for attribute in attributes:
            asset[attribute] = asset['type_fields'][attribute]

        asset.pop('type_fields')

    return json_input


if __name__ == '__main__':
    pull_assets()
