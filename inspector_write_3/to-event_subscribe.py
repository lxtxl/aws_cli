#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/subscribe-to-event.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # resource-arn : The ARN of the assessment template that is used during the event for which you want to receive SNS notifications.
    # event : The event for which you want to receive SNS notifications.
Possible values:

ASSESSMENT_RUN_STARTED
ASSESSMENT_RUN_COMPLETED
ASSESSMENT_RUN_STATE_CHANGED
FINDING_REPORTED
OTHER
    # topic-arn : The ARN of the SNS topic to which the SNS notifications are sent.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("inspector", "subscribe-to-event", "resource-arn", "event", "topic-arn", add_option_dict)
