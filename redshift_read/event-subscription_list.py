#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-event-subscriptions.html
if __name__ == '__main__':
    """
	create-event-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-event-subscription.html
	delete-event-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-event-subscription.html
	modify-event-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-event-subscription.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("redshift", "describe-event-subscriptions", add_option_dict)