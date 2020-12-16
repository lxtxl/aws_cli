#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/update-firewall-policy.html
if __name__ == '__main__':
    """
	associate-firewall-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/associate-firewall-policy.html
	create-firewall-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/create-firewall-policy.html
	delete-firewall-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/delete-firewall-policy.html
	describe-firewall-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/describe-firewall-policy.html
	list-firewall-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/list-firewall-policies.html
    """

    parameter_display_string = """
    # update-token : A token used for optimistic locking. Network Firewall returns a token to your requests that access the firewall policy. The token marks the state of the policy resource at the time of the request.
To make changes to the policy, you provide the token in your request. Network Firewall uses the token to ensure that the policy hasnât changed since you last retrieved it. If it has changed, the operation fails with an InvalidTokenException . If this happens, retrieve the firewall policy again to get a current copy of it with current token. Reapply your changes as needed, then try the operation again using the new token.
    # firewall-policy : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("network-firewall", "update-firewall-policy", "update-token", "firewall-policy", add_option_dict)
