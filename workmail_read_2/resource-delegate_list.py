#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-resource-delegates.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # organization-id : The identifier for the organization that contains the resource for which delegates are listed.
    # resource-id : The identifier for the resource whose delegates are listed.
    """

    execute_two_parameter("workmail", "list-resource-delegates", "organization-id", "resource-id", parameter_display_string)