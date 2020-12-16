#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-user-pool-domain.html
if __name__ == '__main__':
    """
	create-user-pool-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-user-pool-domain.html
	delete-user-pool-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-user-pool-domain.html
	describe-user-pool-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-user-pool-domain.html
    """

    parameter_display_string = """
    # domain : The domain name for the custom domain that hosts the sign-up and sign-in pages for your application. For example: auth.example.com .
This string can include only lowercase letters, numbers, and hyphens. Do not use a hyphen for the first or last character. Use periods to separate subdomain names.
    # user-pool-id : The ID of the user pool that is associated with the custom domain that you are updating the certificate for.
    # custom-domain-config : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("cognito-idp", "update-user-pool-domain", "domain", "user-pool-id", "custom-domain-config", add_option_dict)
