#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/confirm-subscription.html
if __name__ == '__main__':
    """
	list-subscriptions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/list-subscriptions.html
    """

    parameter_display_string = """
    # topic-arn : The ARN of the topic for which you wish to confirm a subscription.
    # token : Short-lived token sent to an endpoint during the Subscribe action.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sns", "confirm-subscription", "topic-arn", "token", add_option_dict)
