#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/create-log-subscription.html
if __name__ == '__main__':
    """
	delete-log-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/delete-log-subscription.html
	list-log-subscriptions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/list-log-subscriptions.html
    """

    parameter_display_string = """
    # directory-id : Identifier of the directory to which you want to subscribe and receive real-time logs to your specified CloudWatch log group.
    # log-group-name : The name of the CloudWatch log group where the real-time domain controller logs are forwarded.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ds", "create-log-subscription", "directory-id", "log-group-name", add_option_dict)
