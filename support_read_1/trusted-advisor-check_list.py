#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-trusted-advisor-checks.html
if __name__ == '__main__':
    """
	refresh-trusted-advisor-check : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/refresh-trusted-advisor-check.html
    """

    parameter_display_string = """
    # language : The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English (âenâ) and Japanese (âjaâ). Language parameters must be passed explicitly for operations that take them.
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

    execute_one_parameter("support", "describe-trusted-advisor-checks", "language", add_option_dict)