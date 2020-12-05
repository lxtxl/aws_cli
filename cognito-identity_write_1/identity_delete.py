#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/delete-identities.html
if __name__ == '__main__':
    """
	describe-identity : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/describe-identity.html
	list-identities : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/list-identities.html
	unlink-identity : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/unlink-identity.html
    """

    parameter_display_string = """
    # identity-ids-to-delete : A list of 1-60 identities that you want to delete.
(string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cognito-identity", "delete-identities", "identity-ids-to-delete", add_option_dict)





