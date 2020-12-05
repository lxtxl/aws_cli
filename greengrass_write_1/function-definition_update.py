#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/update-function-definition.html
if __name__ == '__main__':
    """
	create-function-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-function-definition.html
	delete-function-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/delete-function-definition.html
	get-function-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-function-definition.html
	list-function-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-function-definitions.html
    """

    parameter_display_string = """
    # function-definition-id : The ID of the Lambda function definition.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("greengrass", "update-function-definition", "function-definition-id", add_option_dict)





