#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/create-location-efs.html
if __name__ == '__main__':
    """
	describe-location-efs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/describe-location-efs.html
    """

    parameter_display_string = """
    # efs-filesystem-arn : The Amazon Resource Name (ARN) for the Amazon EFS file system.
    # ec2-config : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("datasync", "create-location-efs", "efs-filesystem-arn", "ec2-config", add_option_dict)
