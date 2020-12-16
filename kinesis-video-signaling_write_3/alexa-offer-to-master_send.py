#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis-video-signaling/send-alexa-offer-to-master.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # channel-arn : The ARN of the signaling channel by which Alexa and the master peer communicate.
    # sender-client-id : The unique identifier for the sender client.
    # message-payload : The base64-encoded SDP offer content.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("kinesis-video-signaling", "send-alexa-offer-to-master", "channel-arn", "sender-client-id", "message-payload", add_option_dict)
