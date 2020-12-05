#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/create-queue.html
if __name__ == '__main__':
    """
	delete-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/delete-queue.html
	list-queues : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/list-queues.html
	purge-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/purge-queue.html
	tag-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/tag-queue.html
	untag-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/untag-queue.html
    """

    parameter_display_string = """
    # queue-name : The name of the new queue. The following limits apply to this name:

A queue name can have up to 80 characters.
Valid values: alphanumeric characters, hyphens (- ), and underscores (_ ).
A FIFO queue name must end with the .fifo suffix.

Queue URLs and names are case-sensitive.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sqs", "create-queue", "queue-name", add_option_dict)





