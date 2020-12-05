#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/create-system-template.html
if __name__ == '__main__':
    """
	delete-system-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/delete-system-template.html
	deprecate-system-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/deprecate-system-template.html
	get-system-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/get-system-template.html
	search-system-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/search-system-templates.html
	update-system-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/update-system-template.html
    """

    parameter_display_string = """
    # definition : 
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iotthingsgraph", "create-system-template", "definition", add_option_dict)





