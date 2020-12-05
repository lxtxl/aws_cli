#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/untag-queue.html
if __name__ == '__main__':
    """
	create-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/create-queue.html
	delete-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/delete-queue.html
	list-queues : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/list-queues.html
	purge-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/purge-queue.html
	tag-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/tag-queue.html
    """

    parameter_display_string = """
    # queue-url : The URL of the queue.
    # tag-keys : The list of tags to be removed from the specified queue.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sqs", "untag-queue", "queue-url", "tag-keys", add_option_dict)
