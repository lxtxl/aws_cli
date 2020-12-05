#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/get-domain-permissions-policy.html
if __name__ == '__main__':
    """
	delete-domain-permissions-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/delete-domain-permissions-policy.html
	put-domain-permissions-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/put-domain-permissions-policy.html
    """

    parameter_display_string = """
    # domain : The name of the domain to which the resource policy is attached.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("codeartifact", "get-domain-permissions-policy", "domain", add_option_dict)