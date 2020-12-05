#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/create-archive.html
if __name__ == '__main__':
    """
	delete-archive : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/delete-archive.html
	describe-archive : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/describe-archive.html
	list-archives : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-archives.html
	update-archive : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/update-archive.html
    """

    parameter_display_string = """
    # archive-name : The name for the archive to create.
    # event-source-arn : The ARN of the event source associated with the archive.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("events", "create-archive", "archive-name", "event-source-arn", add_option_dict)
