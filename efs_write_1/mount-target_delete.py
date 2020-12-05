#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/delete-mount-target.html
if __name__ == '__main__':
    """
	create-mount-target : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/create-mount-target.html
	describe-mount-targets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/describe-mount-targets.html
    """

    parameter_display_string = """
    # mount-target-id : The ID of the mount target to delete (String).
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("efs", "delete-mount-target", "mount-target-id", add_option_dict)





