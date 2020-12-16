#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-rules.html
if __name__ == '__main__':
    """
	associate-resolver-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/associate-resolver-rule.html
	create-resolver-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/create-resolver-rule.html
	delete-resolver-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/delete-resolver-rule.html
	disassociate-resolver-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/disassociate-resolver-rule.html
	get-resolver-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-rule.html
	update-resolver-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/update-resolver-rule.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("route53resolver", "list-resolver-rules", add_option_dict)