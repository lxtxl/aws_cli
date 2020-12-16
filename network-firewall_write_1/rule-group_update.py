#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/update-rule-group.html
if __name__ == '__main__':
    """
	create-rule-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/create-rule-group.html
	delete-rule-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/delete-rule-group.html
	describe-rule-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/describe-rule-group.html
	list-rule-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/list-rule-groups.html
    """

    parameter_display_string = """
    # update-token : A token used for optimistic locking. Network Firewall returns a token to your requests that access the rule group. The token marks the state of the rule group resource at the time of the request.
To make changes to the rule group, you provide the token in your request. Network Firewall uses the token to ensure that the rule group hasnât changed since you last retrieved it. If it has changed, the operation fails with an InvalidTokenException . If this happens, retrieve the rule group again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("network-firewall", "update-rule-group", "update-token", add_option_dict)





