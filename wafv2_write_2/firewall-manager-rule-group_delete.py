#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/delete-firewall-manager-rule-groups.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # web-acl-arn : The Amazon Resource Name (ARN) of the web ACL.
    # web-acl-lock-token : A token used for optimistic locking. AWS WAF returns a token to your get and list requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like update and delete. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a WAFOptimisticLockException . If this happens, perform another get, and use the new token returned by that operation.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("wafv2", "delete-firewall-manager-rule-groups", "web-acl-arn", "web-acl-lock-token", add_option_dict)
