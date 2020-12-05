#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/describe-index-fields.html
if __name__ == '__main__':
    """
	define-index-field : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/define-index-field.html
	delete-index-field : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/delete-index-field.html
    """

    parameter_display_string = """
    # domain-name : The name of the domain you want to describe.
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

    execute_one_parameter("cloudsearch", "describe-index-fields", "domain-name", add_option_dict)