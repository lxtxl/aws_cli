#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/update-file-system.html
if __name__ == '__main__':
    """
	create-file-system : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/create-file-system.html
	delete-file-system : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/delete-file-system.html
	describe-file-systems : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/describe-file-systems.html
    """

    parameter_display_string = """
    # file-system-id : The ID of the file system that you want to update.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("efs", "update-file-system", "file-system-id", add_option_dict)





