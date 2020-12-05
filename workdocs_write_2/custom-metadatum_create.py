#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/create-custom-metadata.html
if __name__ == '__main__':
    """
	delete-custom-metadata : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/delete-custom-metadata.html
    """

    parameter_display_string = """
    # resource-id : The ID of the resource.
    # custom-metadata : Custom metadata in the form of name-value pairs.
key -> (string)
value -> (string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("workdocs", "create-custom-metadata", "resource-id", "custom-metadata", add_option_dict)
