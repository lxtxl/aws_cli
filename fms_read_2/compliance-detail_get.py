#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/get-compliance-detail.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # policy-id : The ID of the policy that you want to get the details for. PolicyId is returned by PutPolicy and by ListPolicies .
    # member-account : The AWS account that owns the resources that you want to get the details for.
    """

    execute_two_parameter("fms", "get-compliance-detail", "policy-id", "member-account", parameter_display_string)