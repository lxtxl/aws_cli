#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/set-ui-customization.html
if __name__ == '__main__':
    """
	get-ui-customization : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-ui-customization.html
    """

    parameter_display_string = """
    # user-pool-id : The user pool ID for the user pool.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cognito-idp", "set-ui-customization", "user-pool-id", add_option_dict)





