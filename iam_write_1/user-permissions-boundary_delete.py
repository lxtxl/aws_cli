#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-user-permissions-boundary.html
if __name__ == '__main__':
    """
	put-user-permissions-boundary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/put-user-permissions-boundary.html
    """

    parameter_display_string = """
    # user-name : The name (friendly name, not ARN) of the IAM user from which you want to remove the permissions boundary.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iam", "delete-user-permissions-boundary", "user-name", add_option_dict)





