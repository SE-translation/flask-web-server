import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

def get_config():

    return json.load(open(dir_path+"\\config.json"))