#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-event-subscription.html
if __name__ == '__main__':
    """
	create-event-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-event-subscription.html
	describe-event-subscriptions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-event-subscriptions.html
	modify-event-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-event-subscription.html
    """

    parameter_display_string = """
    # subscription-name : The name of the DMS event notification subscription to be deleted.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("dms", "delete-event-subscription", "subscription-name", add_option_dict)





