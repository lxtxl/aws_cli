#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/delete-notification-subscription.html
if __name__ == '__main__':
    """
	create-notification-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/create-notification-subscription.html
	describe-notification-subscriptions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-notification-subscriptions.html
    """

    parameter_display_string = """
    # subscription-id : The ID of the subscription.
    # organization-id : The ID of the organization.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("workdocs", "delete-notification-subscription", "subscription-id", "organization-id", add_option_dict)
