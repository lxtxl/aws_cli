#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-launch-template-versions.html
if __name__ == '__main__':
    """
	create-launch-template-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-launch-template-version.html
	describe-launch-template-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-launch-template-versions.html
    """

    parameter_display_string = """
    # versions : The version numbers of one or more launch template versions to delete.
(string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "delete-launch-template-versions", "versions", add_option_dict)





