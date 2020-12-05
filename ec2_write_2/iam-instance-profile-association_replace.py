#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/replace-iam-instance-profile-association.html
if __name__ == '__main__':
    """
	describe-iam-instance-profile-associations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-iam-instance-profile-associations.html
    """

    parameter_display_string = """
    # iam-instance-profile : 
    # association-id : The ID of the existing IAM instance profile association.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "replace-iam-instance-profile-association", "iam-instance-profile", "association-id", add_option_dict)
