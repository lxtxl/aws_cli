#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-namespace.html
if __name__ == '__main__':
    """
	delete-namespace : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-namespace.html
	describe-namespace : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-namespace.html
	list-namespaces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/list-namespaces.html
    """

    parameter_display_string = """
    # aws-account-id : The ID for the AWS account that you want to create the QuickSight namespace in.
    # namespace : The name that you want to use to describe the new namespace.
    # identity-store : Specifies the type of your user identity directory. Currently, this supports users with an identity type of QUICKSIGHT .
Possible values:

QUICKSIGHT
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("quicksight", "create-namespace", "aws-account-id", "namespace", "identity-store", add_option_dict)
