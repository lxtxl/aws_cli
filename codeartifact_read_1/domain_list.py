#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/describe-domain.html
if __name__ == '__main__':
    """
	create-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/create-domain.html
	delete-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/delete-domain.html
	list-domains : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/list-domains.html
    """

    parameter_display_string = """
    # domain : A string that specifies the name of the requested domain.
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

    execute_one_parameter("codeartifact", "describe-domain", "domain", add_option_dict)