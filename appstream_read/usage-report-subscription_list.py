#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-usage-report-subscriptions.html
if __name__ == '__main__':
    """
	create-usage-report-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/create-usage-report-subscription.html
	delete-usage-report-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/delete-usage-report-subscription.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("appstream", "describe-usage-report-subscriptions", add_option_dict)