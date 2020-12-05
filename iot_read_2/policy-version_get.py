#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-policy-version.html
if __name__ == '__main__':
    """
	create-policy-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-policy-version.html
	delete-policy-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-policy-version.html
	list-policy-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-policy-versions.html
    """

    parameter_display_string = """
    # policy-name : The name of the policy.
    # policy-version-id : The policy version ID.
    """

    execute_two_parameter("iot", "get-policy-version", "policy-name", "policy-version-id", parameter_display_string)