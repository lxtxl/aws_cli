#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/get-queue-attributes.html
if __name__ == '__main__':
    """
	set-queue-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/set-queue-attributes.html
    """

    parameter_display_string = """
    # queue-url : The URL of the Amazon SQS queue whose attribute information is retrieved.
Queue URLs and names are case-sensitive.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("sqs", "get-queue-attributes", "queue-url", add_option_dict)