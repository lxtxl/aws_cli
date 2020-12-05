#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/create-accelerator.html
if __name__ == '__main__':
    """
	delete-accelerator : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/delete-accelerator.html
	describe-accelerator : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/describe-accelerator.html
	list-accelerators : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-accelerators.html
	update-accelerator : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/update-accelerator.html
    """

    parameter_display_string = """
    # name : The name of an accelerator. The name can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens (-), and must not begin or end with a hyphen.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("globalaccelerator", "create-accelerator", "name", add_option_dict)





