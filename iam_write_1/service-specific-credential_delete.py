#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-service-specific-credential.html
if __name__ == '__main__':
    """
	create-service-specific-credential : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-service-specific-credential.html
	list-service-specific-credentials : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-service-specific-credentials.html
	reset-service-specific-credential : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/reset-service-specific-credential.html
	update-service-specific-credential : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-service-specific-credential.html
    """

    parameter_display_string = """
    # service-specific-credential-id : The unique identifier of the service-specific credential. You can get this value by calling  ListServiceSpecificCredentials .
This parameter allows (through its regex pattern ) a string of characters that can consist of any upper or lowercased letter or digit.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iam", "delete-service-specific-credential", "service-specific-credential-id", add_option_dict)





