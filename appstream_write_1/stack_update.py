#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/update-stack.html
if __name__ == '__main__':
    """
	create-stack : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/create-stack.html
	delete-stack : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/delete-stack.html
	describe-stacks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-stacks.html
    """

    parameter_display_string = """
    # name : The name of the stack.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("appstream", "update-stack", "name", add_option_dict)





