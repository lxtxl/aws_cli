#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-rule.html
if __name__ == '__main__':
    """
	associate-resolver-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/associate-resolver-rule.html
	create-resolver-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/create-resolver-rule.html
	delete-resolver-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/delete-resolver-rule.html
	disassociate-resolver-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/disassociate-resolver-rule.html
	list-resolver-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-rules.html
	update-resolver-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/update-resolver-rule.html
    """

    parameter_display_string = """
    # resolver-rule-id : The ID of the Resolver rule that you want to get information about.
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

    execute_one_parameter("route53resolver", "get-resolver-rule", "resolver-rule-id", add_option_dict)