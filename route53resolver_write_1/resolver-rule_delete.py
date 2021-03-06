#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/delete-resolver-rule.html
if __name__ == '__main__':
    """
	associate-resolver-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/associate-resolver-rule.html
	create-resolver-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/create-resolver-rule.html
	disassociate-resolver-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/disassociate-resolver-rule.html
	get-resolver-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-rule.html
	list-resolver-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-rules.html
	update-resolver-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/update-resolver-rule.html
    """

    parameter_display_string = """
    # resolver-rule-id : The ID of the Resolver rule that you want to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("route53resolver", "delete-resolver-rule", "resolver-rule-id", add_option_dict)





