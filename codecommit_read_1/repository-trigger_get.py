#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-repository-triggers.html
if __name__ == '__main__':
    """
	put-repository-triggers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/put-repository-triggers.html
	test-repository-triggers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/test-repository-triggers.html
    """

    parameter_display_string = """
    # repository-name : The name of the repository for which the trigger is configured.
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

    execute_one_parameter("codecommit", "get-repository-triggers", "repository-name", add_option_dict)