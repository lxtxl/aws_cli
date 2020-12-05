import os
import json
import sys

def read_setting_file():
    if not os.path.isfile("config/setting.json"):
        print("setting.json is not exist")
        sys.exit(1)

    with open("config/setting.json", "r") as f:
        setting_config = json.load(f)

    return setting_config

def read_work_profile_file(parameter):
    work_profile = parameter
    work_profile_json = "config/{}.json".format(work_profile)

    if not os.path.isfile(work_profile_json):
        print(work_profile_json, "is not exist")
        sys.exit(1)

    with open(work_profile_json, "r") as f:
        profile_config = json.load(f)

    return profile_config