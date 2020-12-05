#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/create-folder.html
if __name__ == '__main__':
    """
	delete-folder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/delete-folder.html
	get-folder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/get-folder.html
	update-folder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/update-folder.html
    """

    parameter_display_string = """
    # parent-folder-id : The ID of the parent folder.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("workdocs", "create-folder", "parent-folder-id", add_option_dict)





