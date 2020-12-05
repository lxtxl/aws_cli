#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-function-definition-version.html
if __name__ == '__main__':
    """
	get-function-definition-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-function-definition-version.html
	list-function-definition-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-function-definition-versions.html
    """

    parameter_display_string = """
    # function-definition-id : The ID of the Lambda function definition.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("greengrass", "create-function-definition-version", "function-definition-id", add_option_dict)





