#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-rule-association.html
if __name__ == '__main__':
    """
	list-resolver-rule-associations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-rule-associations.html
    """

    parameter_display_string = """
    # resolver-rule-association-id : The ID of the Resolver rule association that you want to get information about.
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

    execute_one_parameter("route53resolver", "get-resolver-rule-association", "resolver-rule-association-id", add_option_dict)