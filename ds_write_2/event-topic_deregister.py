#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/deregister-event-topic.html
if __name__ == '__main__':
    """
	describe-event-topics : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/describe-event-topics.html
	register-event-topic : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/register-event-topic.html
    """

    parameter_display_string = """
    # directory-id : The Directory ID to remove as a publisher. This directory will no longer send messages to the specified SNS topic.
    # topic-name : The name of the SNS topic from which to remove the directory as a publisher.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ds", "deregister-event-topic", "directory-id", "topic-name", add_option_dict)
