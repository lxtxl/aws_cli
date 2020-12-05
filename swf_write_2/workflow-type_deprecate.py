#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/deprecate-workflow-type.html
if __name__ == '__main__':
    """
	describe-workflow-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/describe-workflow-type.html
	list-workflow-types : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/list-workflow-types.html
	register-workflow-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/register-workflow-type.html
	undeprecate-workflow-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/undeprecate-workflow-type.html
    """

    parameter_display_string = """
    # domain : The name of the domain in which the workflow type is registered.
    # workflow-type : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("swf", "deprecate-workflow-type", "domain", "workflow-type", add_option_dict)
