#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/change-message-visibility.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # queue-url : The URL of the Amazon SQS queue whose messageâs visibility is changed.
Queue URLs and names are case-sensitive.
    # receipt-handle : The receipt handle associated with the message whose visibility timeout is changed. This parameter is returned by the ``  ReceiveMessage `` action.
    # visibility-timeout : The new value for the messageâs visibility timeout (in seconds). Values range: 0 to 43200 . Maximum: 12 hours.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("sqs", "change-message-visibility", "queue-url", "receipt-handle", "visibility-timeout", add_option_dict)
