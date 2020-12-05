#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-policy-version.html
if __name__ == '__main__':
    """
	create-policy-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-policy-version.html
	delete-policy-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-policy-version.html
	list-policy-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-policy-versions.html
    """

    parameter_display_string = """
    # policy-arn : The Amazon Resource Name (ARN) of the managed policy that you want information about.
For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
    # version-id : Identifies the policy version to retrieve.
This parameter allows (through its regex pattern ) a string of characters that consists of the lowercase letter âvâ followed by one or two digits, and optionally followed by a period â.â and a string of letters and digits.
    """

    execute_two_parameter("iam", "get-policy-version", "policy-arn", "version-id", parameter_display_string)