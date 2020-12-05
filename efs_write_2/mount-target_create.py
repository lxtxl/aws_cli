#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/create-mount-target.html
if __name__ == '__main__':
    """
	delete-mount-target : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/delete-mount-target.html
	describe-mount-targets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/describe-mount-targets.html
    """

    parameter_display_string = """
    # file-system-id : The ID of the file system for which to create the mount target.
    # subnet-id : The ID of the subnet to add the mount target in.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("efs", "create-mount-target", "file-system-id", "subnet-id", add_option_dict)
