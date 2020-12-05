#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/delete-message-batch.html
if __name__ == '__main__':
    """
	send-message-batch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/send-message-batch.html
    """

    parameter_display_string = """
    # queue-url : The URL of the Amazon SQS queue from which messages are deleted.
Queue URLs and names are case-sensitive.
    # entries : A list of receipt handles for the messages to be deleted.
(structure)

Encloses a receipt handle and an identifier for it.
Id -> (string)

An identifier for this particular receipt handle. This is used to communicate the result.

Note
The Id s of a batch request need to be unique within a request.
This identifier can have up to 80 characters. The following characters are accepted: alphanumeric characters, hyphens(-), and underscores (_).


ReceiptHandle -> (string)

A receipt handle.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sqs", "delete-message-batch", "queue-url", "entries", add_option_dict)
