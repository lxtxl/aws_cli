#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/put-backup-policy.html
if __name__ == '__main__':
    """
	describe-backup-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/describe-backup-policy.html
    """

    parameter_display_string = """
    # file-system-id : Specifies which EFS file system to update the backup policy for.
    # backup-policy : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("efs", "put-backup-policy", "file-system-id", "backup-policy", add_option_dict)
