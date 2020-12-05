#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/associate-entity-to-thing.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # thing-name : The name of the thing to which the entity is to be associated.
    # entity-id : The ID of the device to be associated with the thing.
The ID should be in the following format.

urn:tdm:REGION/ACCOUNT ID/default:device:DEVICENAME
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iotthingsgraph", "associate-entity-to-thing", "thing-name", "entity-id", add_option_dict)
