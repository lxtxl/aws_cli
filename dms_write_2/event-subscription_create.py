#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-event-subscription.html
if __name__ == '__main__':
    """
	delete-event-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-event-subscription.html
	describe-event-subscriptions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-event-subscriptions.html
	modify-event-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-event-subscription.html
    """

    parameter_display_string = """
    # subscription-name : The name of the AWS DMS event notification subscription. This name must be less than 255 characters.
    # sns-topic-arn : The Amazon Resource Name (ARN) of the Amazon SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("dms", "create-event-subscription", "subscription-name", "sns-topic-arn", add_option_dict)
