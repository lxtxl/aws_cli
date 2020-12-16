#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-instance-export-task.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # export-to-s3-task : 
    # instance-id : The ID of the instance.
    # target-environment : The target virtualization environment.
Possible values:

citrix
vmware
microsoft
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ec2", "create-instance-export-task", "export-to-s3-task", "instance-id", "target-environment", add_option_dict)
