#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-service-specific-credential.html
if __name__ == '__main__':
    """
	create-service-specific-credential : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-service-specific-credential.html
	delete-service-specific-credential : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-service-specific-credential.html
	list-service-specific-credentials : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-service-specific-credentials.html
	reset-service-specific-credential : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/reset-service-specific-credential.html
    """

    parameter_display_string = """
    # service-specific-credential-id : The unique identifier of the service-specific credential.
This parameter allows (through its regex pattern ) a string of characters that can consist of any upper or lowercased letter or digit.
    # status : The status to be assigned to the service-specific credential.
Possible values:

Active
Inactive
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iam", "update-service-specific-credential", "service-specific-credential-id", "status", add_option_dict)
