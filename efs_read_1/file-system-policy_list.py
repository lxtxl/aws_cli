#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/describe-file-system-policy.html
if __name__ == '__main__':
    """
	delete-file-system-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/delete-file-system-policy.html
	put-file-system-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/put-file-system-policy.html
    """

    parameter_display_string = """
    # file-system-id : Specifies which EFS file system to retrieve the FileSystemPolicy for.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("efs", "describe-file-system-policy", "file-system-id", add_option_dict)