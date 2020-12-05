#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-user-pool-domain.html
if __name__ == '__main__':
    """
	delete-user-pool-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-user-pool-domain.html
	describe-user-pool-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-user-pool-domain.html
	update-user-pool-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-user-pool-domain.html
    """

    parameter_display_string = """
    # domain : The domain string.
    # user-pool-id : The user pool ID.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cognito-idp", "create-user-pool-domain", "domain", "user-pool-id", add_option_dict)
