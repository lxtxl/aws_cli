#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/delete-domain-permissions-policy.html
if __name__ == '__main__':
    """
	get-domain-permissions-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/get-domain-permissions-policy.html
	put-domain-permissions-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/put-domain-permissions-policy.html
    """

    parameter_display_string = """
    # domain : The name of the domain associated with the resource policy to be deleted.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("codeartifact", "delete-domain-permissions-policy", "domain", add_option_dict)





