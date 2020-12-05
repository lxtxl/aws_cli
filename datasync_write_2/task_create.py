#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/create-task.html
if __name__ == '__main__':
    """
	delete-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/delete-task.html
	describe-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/describe-task.html
	list-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/list-tasks.html
	update-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/update-task.html
    """

    parameter_display_string = """
    # source-location-arn : The Amazon Resource Name (ARN) of the source location for the task.
    # destination-location-arn : The Amazon Resource Name (ARN) of an AWS storage resourceâs location.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("datasync", "create-task", "source-location-arn", "destination-location-arn", add_option_dict)
