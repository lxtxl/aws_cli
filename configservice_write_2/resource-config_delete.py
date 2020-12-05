#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-resource-config.html
if __name__ == '__main__':
    """
	put-resource-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-resource-config.html
	select-resource-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/select-resource-config.html
    """

    parameter_display_string = """
    # resource-type : The type of the resource.
    # resource-id : Unique identifier of the resource.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("configservice", "delete-resource-config", "resource-type", "resource-id", add_option_dict)
