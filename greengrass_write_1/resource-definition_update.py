#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/update-resource-definition.html
if __name__ == '__main__':
    """
	create-resource-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-resource-definition.html
	delete-resource-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/delete-resource-definition.html
	get-resource-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-resource-definition.html
	list-resource-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-resource-definitions.html
    """

    parameter_display_string = """
    # resource-definition-id : The ID of the resource definition.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("greengrass", "update-resource-definition", "resource-definition-id", add_option_dict)





