#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/update-resource.html
if __name__ == '__main__':
    """
	deregister-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/deregister-resource.html
	describe-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/describe-resource.html
	list-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/list-resources.html
	register-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/register-resource.html
    """

    parameter_display_string = """
    # role-arn : The new role to use for the given resource registered in AWS Lake Formation.
    # resource-arn : The resource ARN.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lakeformation", "update-resource", "role-arn", "resource-arn", add_option_dict)
