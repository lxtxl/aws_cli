#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents-data/batch-put-message.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # messages : The list of messages to send. Each message has the following format: '{ "messageId": "string", "inputName": "string", "payload": "string"}'
(structure)

Information about a message.
messageId -> (string)

The ID to assign to the message. Within each batch sent, each "messageId" must be unique.

inputName -> (string)

The name of the input into which the message payload is transformed.

payload -> (blob)

The payload of the message. This can be a JSON string or a Base-64-encoded string representing binary data (in which case you must decode it).
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iotevents-data", "batch-put-message", "messages", add_option_dict)





