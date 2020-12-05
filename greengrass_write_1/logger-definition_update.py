#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/update-logger-definition.html
if __name__ == '__main__':
    """
	create-logger-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-logger-definition.html
	delete-logger-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/delete-logger-definition.html
	get-logger-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-logger-definition.html
	list-logger-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-logger-definitions.html
    """

    parameter_display_string = """
    # logger-definition-id : The ID of the logger definition.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("greengrass", "update-logger-definition", "logger-definition-id", add_option_dict)





