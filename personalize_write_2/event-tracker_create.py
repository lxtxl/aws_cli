#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/create-event-tracker.html
if __name__ == '__main__':
    """
	delete-event-tracker : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/delete-event-tracker.html
	describe-event-tracker : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/describe-event-tracker.html
	list-event-trackers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/list-event-trackers.html
    """

    parameter_display_string = """
    # name : The name for the event tracker.
    # dataset-group-arn : The Amazon Resource Name (ARN) of the dataset group that receives the event data.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("personalize", "create-event-tracker", "name", "dataset-group-arn", add_option_dict)
