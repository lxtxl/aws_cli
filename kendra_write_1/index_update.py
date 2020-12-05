#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/update-index.html
if __name__ == '__main__':
    """
	create-index : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/create-index.html
	delete-index : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/delete-index.html
	describe-index : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/describe-index.html
    """

    parameter_display_string = """
    # id : The identifier of the index to update.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("kendra", "update-index", "id", add_option_dict)





