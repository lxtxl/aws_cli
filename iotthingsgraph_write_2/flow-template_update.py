#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/update-flow-template.html
if __name__ == '__main__':
    """
	create-flow-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/create-flow-template.html
	delete-flow-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/delete-flow-template.html
	deprecate-flow-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/deprecate-flow-template.html
	get-flow-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/get-flow-template.html
	search-flow-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/search-flow-templates.html
    """

    parameter_display_string = """
    # id : The ID of the workflow to be updated.
The ID should be in the following format.

urn:tdm:REGION/ACCOUNT ID/default:workflow:WORKFLOWNAME
    # definition : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iotthingsgraph", "update-flow-template", "id", "definition", add_option_dict)
