#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/dissociate-entity-from-thing.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # thing-name : The name of the thing to disassociate.
    # entity-type : The entity type from which to disassociate the thing.
Possible values:

DEVICE
SERVICE
DEVICE_MODEL
CAPABILITY
STATE
ACTION
EVENT
PROPERTY
MAPPING
ENUM
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iotthingsgraph", "dissociate-entity-from-thing", "thing-name", "entity-type", add_option_dict)
