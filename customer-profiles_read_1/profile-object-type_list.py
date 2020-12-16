#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/list-profile-object-types.html
if __name__ == '__main__':
    """
	delete-profile-object-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/delete-profile-object-type.html
	get-profile-object-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/get-profile-object-type.html
	put-profile-object-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/put-profile-object-type.html
    """

    parameter_display_string = """
    # domain-name : The unique name of the domain.
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

    execute_one_parameter("customer-profiles", "list-profile-object-types", "domain-name", add_option_dict)