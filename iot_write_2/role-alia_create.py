#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-role-alias.html
if __name__ == '__main__':
    """
	delete-role-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-role-alias.html
	describe-role-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-role-alias.html
	update-role-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-role-alias.html
    """

    parameter_display_string = """
    # role-alias : The role alias that points to a role ARN. This allows you to change the role without having to update the device.
    # role-arn : The role ARN.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iot", "create-role-alias", "role-alias", "role-arn", add_option_dict)
