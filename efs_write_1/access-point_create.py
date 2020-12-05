#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/create-access-point.html
if __name__ == '__main__':
    """
	delete-access-point : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/delete-access-point.html
	describe-access-points : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/describe-access-points.html
    """

    parameter_display_string = """
    # file-system-id : The ID of the EFS file system that the access point provides access to.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("efs", "create-access-point", "file-system-id", add_option_dict)





