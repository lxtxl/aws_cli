#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/put-application-policy.html
if __name__ == '__main__':
    """
	get-application-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/get-application-policy.html
    """

    parameter_display_string = """
    # application-id : The Amazon Resource Name (ARN) of the application.
    # statements : An array of policy statements applied to the application.
(structure)

Policy statement applied to the application.
Actions -> (list)

For the list of actions supported for this operation, see Application Permissions .
(string)

PrincipalOrgIDs -> (list)

An array of PrinciplalOrgIDs, which corresponds to AWS IAM aws:PrincipalOrgID global condition key.
(string)

Principals -> (list)

An array of AWS account IDs, or * to make the application public.
(string)

StatementId -> (string)

A unique ID for the statement.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("serverlessrepo", "put-application-policy", "application-id", "statements", add_option_dict)
