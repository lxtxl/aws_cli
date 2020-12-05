#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/put-file-system-policy.html
if __name__ == '__main__':
    """
	delete-file-system-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/delete-file-system-policy.html
	describe-file-system-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/describe-file-system-policy.html
    """

    parameter_display_string = """
    # file-system-id : The ID of the EFS file system that you want to create or update the FileSystemPolicy for.
    # policy : The FileSystemPolicy that youâre creating. Accepts a JSON formatted policy definition. To find out more about the elements that make up a file system policy, see EFS Resource-based Policies .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("efs", "put-file-system-policy", "file-system-id", "policy", add_option_dict)
