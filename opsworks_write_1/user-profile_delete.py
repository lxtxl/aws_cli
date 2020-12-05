#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/delete-user-profile.html
if __name__ == '__main__':
    """
	create-user-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/create-user-profile.html
	describe-user-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-user-profiles.html
	update-user-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-user-profile.html
    """

    parameter_display_string = """
    # iam-user-arn : The userâs IAM ARN. This can also be a federated userâs ARN.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("opsworks", "delete-user-profile", "iam-user-arn", add_option_dict)





