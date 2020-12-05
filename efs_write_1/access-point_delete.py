#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/delete-access-point.html
if __name__ == '__main__':
    """
	create-access-point : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/create-access-point.html
	describe-access-points : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/describe-access-points.html
    """

    parameter_display_string = """
    # access-point-id : The ID of the access point that you want to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("efs", "delete-access-point", "access-point-id", add_option_dict)





