#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/undeprecate-activity-type.html
if __name__ == '__main__':
    """
	deprecate-activity-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/deprecate-activity-type.html
	describe-activity-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/describe-activity-type.html
	list-activity-types : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/list-activity-types.html
	register-activity-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/register-activity-type.html
    """

    parameter_display_string = """
    # domain : The name of the domain of the deprecated activity type.
    # activity-type : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("swf", "undeprecate-activity-type", "domain", "activity-type", add_option_dict)
