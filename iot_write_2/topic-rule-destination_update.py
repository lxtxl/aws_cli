#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-topic-rule-destination.html
if __name__ == '__main__':
    """
	confirm-topic-rule-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/confirm-topic-rule-destination.html
	create-topic-rule-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-topic-rule-destination.html
	delete-topic-rule-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-topic-rule-destination.html
	get-topic-rule-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-topic-rule-destination.html
	list-topic-rule-destinations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-topic-rule-destinations.html
    """

    parameter_display_string = """
    # arn : The ARN of the topic rule destination.
    # status : The status of the topic rule destination. Valid values are:

IN_PROGRESS

A topic rule destination was created but has not been confirmed. You can set status to IN_PROGRESS by calling UpdateTopicRuleDestination . Calling UpdateTopicRuleDestination causes a new confirmation challenge to be sent to your confirmation endpoint.

ENABLED

Confirmation was completed, and traffic to this destination is allowed. You can set status to DISABLED by calling UpdateTopicRuleDestination .

DISABLED

Confirmation was completed, and traffic to this destination is not allowed. You can set status to ENABLED by calling UpdateTopicRuleDestination .

ERROR

Confirmation could not be completed, for example if the confirmation timed out. You can call GetTopicRuleDestination for details about the error. You can set status to IN_PROGRESS by calling UpdateTopicRuleDestination . Calling UpdateTopicRuleDestination causes a new confirmation challenge to be sent to your confirmation endpoint.
Possible values:

ENABLED
IN_PROGRESS
DISABLED
ERROR
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iot", "update-topic-rule-destination", "arn", "status", add_option_dict)
