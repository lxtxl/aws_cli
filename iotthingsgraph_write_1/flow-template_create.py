#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/create-flow-template.html
if __name__ == '__main__':
    """
	delete-flow-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/delete-flow-template.html
	deprecate-flow-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/deprecate-flow-template.html
	get-flow-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/get-flow-template.html
	search-flow-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/search-flow-templates.html
	update-flow-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/update-flow-template.html
    """

    parameter_display_string = """
    # definition : 
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iotthingsgraph", "create-flow-template", "definition", add_option_dict)





