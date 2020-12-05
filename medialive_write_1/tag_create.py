#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/create-tags.html
if __name__ == '__main__':
    """
	delete-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/delete-tags.html
    """

    parameter_display_string = """
    # resource-arn : Placeholder documentation for __string
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("medialive", "create-tags", "resource-arn", add_option_dict)





