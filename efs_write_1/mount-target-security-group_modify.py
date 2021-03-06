#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/modify-mount-target-security-groups.html
if __name__ == '__main__':
    """
	describe-mount-target-security-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/describe-mount-target-security-groups.html
    """

    parameter_display_string = """
    # mount-target-id : The ID of the mount target whose security groups you want to modify.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("efs", "modify-mount-target-security-groups", "mount-target-id", add_option_dict)





