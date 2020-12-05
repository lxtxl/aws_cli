#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/set-subscription-attributes.html
if __name__ == '__main__':
    """
	get-subscription-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/get-subscription-attributes.html
    """

    parameter_display_string = """
    # subscription-arn : The ARN of the subscription to modify.
    # attribute-name : A map of attributes with their corresponding values.
The following lists the names, descriptions, and values of the special request parameters that the SetTopicAttributes action uses:

DeliveryPolicy â The policy that defines how Amazon SNS retries failed deliveries to HTTP/S endpoints.
FilterPolicy â The simple JSON object that lets your subscriber receive only a subset of messages, rather than receiving every message published to the topic.
RawMessageDelivery â When set to true , enables raw message delivery to Amazon SQS or HTTP/S endpoints. This eliminates the need for the endpoints to process JSON formatting, which is otherwise created for Amazon SNS metadata.
RedrivePolicy â When specified, sends undeliverable messages to the specified Amazon SQS dead-letter queue. Messages that canât be delivered due to client errors (for example, when the subscribed endpoint is unreachable) or server errors (for example, when the service that powers the subscribed endpoint becomes unavailable) are held in the dead-letter queue for further analysis or reprocessing.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sns", "set-subscription-attributes", "subscription-arn", "attribute-name", add_option_dict)
