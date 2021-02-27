"""
This file define function for loading variable value from json file.
"""
import json


def get_token():
    """
    Load discord bot token from parameter.json.

    :return str: 'bot-token' variable from parameter.json
    """
    with open('./parameter.json', 'r') as file:
        json_data = json.load(file)

    file.close()
    return json_data['bot-token']

