#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-iam-instance-profile.html
if __name__ == '__main__':
    """
	disassociate-iam-instance-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disassociate-iam-instance-profile.html
    """

    parameter_display_string = """
    # iam-instance-profile : 
    # instance-id : The ID of the instance.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "associate-iam-instance-profile", "iam-instance-profile", "instance-id", add_option_dict)
