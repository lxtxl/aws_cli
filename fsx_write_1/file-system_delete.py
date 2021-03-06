#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/delete-file-system.html
if __name__ == '__main__':
    """
	create-file-system : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/create-file-system.html
	describe-file-systems : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/describe-file-systems.html
	update-file-system : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/update-file-system.html
    """

    parameter_display_string = """
    # file-system-id : The ID of the file system you want to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("fsx", "delete-file-system", "file-system-id", add_option_dict)





