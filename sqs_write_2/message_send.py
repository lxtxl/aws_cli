#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/send-message.html
if __name__ == '__main__':
    """
	delete-message : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/delete-message.html
	receive-message : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/receive-message.html
    """

    parameter_display_string = """
    # queue-url : The URL of the Amazon SQS queue to which a message is sent.
Queue URLs and names are case-sensitive.
    # message-body : The message to send. The minimum size is one character. The maximum size is 256 KB.

Warning
A message can include only XML, JSON, and unformatted text. The following Unicode characters are allowed:

#x9 | #xA | #xD | #x20 to #xD7FF | #xE000 to #xFFFD | #x10000 to #x10FFFF

Any characters not included in this list will be rejected. For more information, see the W3C specification for characters .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sqs", "send-message", "queue-url", "message-body", add_option_dict)
