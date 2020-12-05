#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/delete-repository-permissions-policy.html
if __name__ == '__main__':
    """
	get-repository-permissions-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/get-repository-permissions-policy.html
	put-repository-permissions-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/put-repository-permissions-policy.html
    """

    parameter_display_string = """
    # domain : The name of the domain that contains the repository associated with the resource policy to be deleted.
    # repository : The name of the repository that is associated with the resource policy to be deleted
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codeartifact", "delete-repository-permissions-policy", "domain", "repository", add_option_dict)
