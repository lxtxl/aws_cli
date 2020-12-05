#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-create-account-status.html
if __name__ == '__main__':
    """
	list-create-account-status : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-create-account-status.html
    """

    parameter_display_string = """
    # create-account-request-id : Specifies the Id value that uniquely identifies the CreateAccount request. You can get the value from the CreateAccountStatus.Id response in an earlier  CreateAccount request, or from the  ListCreateAccountStatus operation.
The regex pattern for a create account request ID string requires âcar-â followed by from 8 to 32 lowercase letters or digits.
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

    execute_one_parameter("organizations", "describe-create-account-status", "create-account-request-id", add_option_dict)