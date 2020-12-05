#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/list-queues.html
if __name__ == '__main__':
    """
	create-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/create-queue.html
	delete-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/delete-queue.html
	purge-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/purge-queue.html
	tag-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/tag-queue.html
	untag-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/untag-queue.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("sqs", "list-queues", add_option_dict)