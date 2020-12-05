#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/delete-anomaly-subscription.html
if __name__ == '__main__':
    """
	create-anomaly-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/create-anomaly-subscription.html
	get-anomaly-subscriptions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-anomaly-subscriptions.html
	update-anomaly-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/update-anomaly-subscription.html
    """

    parameter_display_string = """
    # subscription-arn : The unique identifier of the cost anomaly subscription that you want to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ce", "delete-anomaly-subscription", "subscription-arn", add_option_dict)





