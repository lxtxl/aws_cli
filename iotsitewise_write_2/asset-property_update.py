#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-asset-property.html
if __name__ == '__main__':
    """
	describe-asset-property : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-asset-property.html
    """

    parameter_display_string = """
    # asset-id : The ID of the asset to be updated.
    # property-id : The ID of the asset property to be updated.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iotsitewise", "update-asset-property", "asset-id", "property-id", add_option_dict)
