#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/delete-message.html
if __name__ == '__main__':
    """
	receive-message : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/receive-message.html
	send-message : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/send-message.html
    """

    parameter_display_string = """
    # queue-url : The URL of the Amazon SQS queue from which messages are deleted.
Queue URLs and names are case-sensitive.
    # receipt-handle : The receipt handle associated with the message to delete.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sqs", "delete-message", "queue-url", "receipt-handle", add_option_dict)
