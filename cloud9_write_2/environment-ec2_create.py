#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/create-environment-ec2.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # name : The name of the environment to create.
This name is visible to other AWS IAM users in the same AWS account.
    # instance-type : The type of instance to connect to the environment (for example, t2.micro ).
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloud9", "create-environment-ec2", "name", "instance-type", add_option_dict)
