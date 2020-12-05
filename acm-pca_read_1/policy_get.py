#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/get-policy.html
if __name__ == '__main__':
    """
	delete-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/delete-policy.html
	put-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/put-policy.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Number (ARN) of the private CA that will have its policy retrieved. You can find the CAâs ARN by calling the ListCertificateAuthorities action.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("acm-pca", "get-policy", "resource-arn", add_option_dict)