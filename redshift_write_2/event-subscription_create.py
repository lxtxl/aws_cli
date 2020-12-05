#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-event-subscription.html
if __name__ == '__main__':
    """
	delete-event-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-event-subscription.html
	describe-event-subscriptions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-event-subscriptions.html
	modify-event-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-event-subscription.html
    """

    parameter_display_string = """
    # subscription-name : The name of the event subscription to be created.
Constraints:

Cannot be null, empty, or blank.
Must contain from 1 to 255 alphanumeric characters or hyphens.
First character must be a letter.
Cannot end with a hyphen or contain two consecutive hyphens.
    # sns-topic-arn : The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications. The ARN is created by Amazon SNS when you create a topic and subscribe to it.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("redshift", "create-event-subscription", "subscription-name", "sns-topic-arn", add_option_dict)
