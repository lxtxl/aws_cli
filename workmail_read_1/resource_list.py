#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-resources.html
if __name__ == '__main__':
    """
	create-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/create-resource.html
	delete-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-resource.html
	describe-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-resource.html
	tag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/tag-resource.html
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/untag-resource.html
	update-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/update-resource.html
    """

    parameter_display_string = """
    # organization-id : The identifier for the organization under which the resources exist.
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

    execute_one_parameter("workmail", "list-resources", "organization-id", add_option_dict)