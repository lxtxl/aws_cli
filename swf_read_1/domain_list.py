#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/describe-domain.html
if __name__ == '__main__':
    """
	deprecate-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/deprecate-domain.html
	list-domains : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/list-domains.html
	register-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/register-domain.html
	undeprecate-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/undeprecate-domain.html
    """

    parameter_display_string = """
    # name : The name of the domain to describe.
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

    execute_one_parameter("swf", "describe-domain", "name", add_option_dict)