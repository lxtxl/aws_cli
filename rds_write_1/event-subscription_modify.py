#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-event-subscription.html
if __name__ == '__main__':
    """
	create-event-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-event-subscription.html
	delete-event-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-event-subscription.html
	describe-event-subscriptions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-event-subscriptions.html
    """

    parameter_display_string = """
    # subscription-name : The name of the RDS event notification subscription.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rds", "modify-event-subscription", "subscription-name", add_option_dict)





