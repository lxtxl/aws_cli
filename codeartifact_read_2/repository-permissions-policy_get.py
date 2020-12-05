#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/get-repository-permissions-policy.html
if __name__ == '__main__':
    """
	delete-repository-permissions-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/delete-repository-permissions-policy.html
	put-repository-permissions-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/put-repository-permissions-policy.html
    """

    parameter_display_string = """
    # domain : The name of the domain containing the repository whose associated resource policy is to be retrieved.
    # repository : The name of the repository whose associated resource policy is to be retrieved.
    """

    execute_two_parameter("codeartifact", "get-repository-permissions-policy", "domain", "repository", parameter_display_string)