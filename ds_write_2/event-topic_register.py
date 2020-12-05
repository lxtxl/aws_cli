#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/register-event-topic.html
if __name__ == '__main__':
    """
	deregister-event-topic : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/deregister-event-topic.html
	describe-event-topics : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/describe-event-topics.html
    """

    parameter_display_string = """
    # directory-id : The Directory ID that will publish status messages to the SNS topic.
    # topic-name : The SNS topic name to which the directory will publish status messages. This SNS topic must be in the same region as the specified Directory ID.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ds", "register-event-topic", "directory-id", "topic-name", add_option_dict)
