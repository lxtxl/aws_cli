#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/receive-message.html
if __name__ == '__main__':
    """
	delete-message : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/delete-message.html
	send-message : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/send-message.html
    """

    parameter_display_string = """
    # queue-url : The URL of the Amazon SQS queue from which messages are received.
Queue URLs and names are case-sensitive.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sqs", "receive-message", "queue-url", add_option_dict)





