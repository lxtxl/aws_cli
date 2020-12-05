#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/subscribe.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # topic-arn : The ARN of the topic you want to subscribe to.
    # protocol : The protocol you want to use. Supported protocols include:

http â delivery of JSON-encoded message via HTTP POST
https â delivery of JSON-encoded message via HTTPS POST
email â delivery of message via SMTP
email-json â delivery of JSON-encoded message via SMTP
sms â delivery of message via SMS
sqs â delivery of JSON-encoded message to an Amazon SQS queue
application â delivery of JSON-encoded message to an EndpointArn for a mobile app and device.
lambda â delivery of JSON-encoded message to an Amazon Lambda function.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sns", "subscribe", "topic-arn", "protocol", add_option_dict)
