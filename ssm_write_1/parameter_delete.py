#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-parameter.html
if __name__ == '__main__':
    """
	delete-parameters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-parameters.html
	describe-parameters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-parameters.html
	get-parameter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-parameter.html
	get-parameters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-parameters.html
	put-parameter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/put-parameter.html
    """

    parameter_display_string = """
    # name : The name of the parameter to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ssm", "delete-parameter", "name", add_option_dict)





