#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/deregister-resource.html
if __name__ == '__main__':
    """
	describe-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/describe-resource.html
	list-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/list-resources.html
	register-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/register-resource.html
	update-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/update-resource.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the resource that you want to deregister.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("lakeformation", "deregister-resource", "resource-arn", add_option_dict)





