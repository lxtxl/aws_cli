#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-user-hierarchy-structure.html
if __name__ == '__main__':
    """
	describe-user-hierarchy-structure : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-user-hierarchy-structure.html
    """

    parameter_display_string = """
    # hierarchy-structure : 
    # instance-id : The identifier of the Amazon Connect instance.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("connect", "update-user-hierarchy-structure", "hierarchy-structure", "instance-id", add_option_dict)
