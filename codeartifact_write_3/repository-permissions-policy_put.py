#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/put-repository-permissions-policy.html
if __name__ == '__main__':
    """
	delete-repository-permissions-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/delete-repository-permissions-policy.html
	get-repository-permissions-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/get-repository-permissions-policy.html
    """

    parameter_display_string = """
    # domain : The name of the domain containing the repository to set the resource policy on.
    # repository : The name of the repository to set the resource policy on.
    # policy-document : A valid displayable JSON Aspen policy string to be set as the access control resource policy on the provided repository.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("codeartifact", "put-repository-permissions-policy", "domain", "repository", "policy-document", add_option_dict)
