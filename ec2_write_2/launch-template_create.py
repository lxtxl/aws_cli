#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-launch-template.html
if __name__ == '__main__':
    """
	delete-launch-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-launch-template.html
	describe-launch-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-launch-templates.html
	modify-launch-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-launch-template.html
    """

    parameter_display_string = """
    # launch-template-name : A name for the launch template.
    # launch-template-data : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "create-launch-template", "launch-template-name", "launch-template-data", add_option_dict)
