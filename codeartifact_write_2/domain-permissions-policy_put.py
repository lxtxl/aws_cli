#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/put-domain-permissions-policy.html
if __name__ == '__main__':
    """
	delete-domain-permissions-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/delete-domain-permissions-policy.html
	get-domain-permissions-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/get-domain-permissions-policy.html
    """

    parameter_display_string = """
    # domain : The name of the domain on which to set the resource policy.
    # policy-document : A valid displayable JSON Aspen policy string to be set as the access control resource policy on the provided domain.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codeartifact", "put-domain-permissions-policy", "domain", "policy-document", add_option_dict)
