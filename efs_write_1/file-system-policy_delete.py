#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/delete-file-system-policy.html
if __name__ == '__main__':
    """
	describe-file-system-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/describe-file-system-policy.html
	put-file-system-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/put-file-system-policy.html
    """

    parameter_display_string = """
    # file-system-id : Specifies the EFS file system for which to delete the FileSystemPolicy .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("efs", "delete-file-system-policy", "file-system-id", add_option_dict)





