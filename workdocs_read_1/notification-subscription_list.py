#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-notification-subscriptions.html
if __name__ == '__main__':
    """
	create-notification-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/create-notification-subscription.html
	delete-notification-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/delete-notification-subscription.html
    """

    parameter_display_string = """
    # organization-id : The ID of the organization.
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

    execute_one_parameter("workdocs", "describe-notification-subscriptions", "organization-id", add_option_dict)