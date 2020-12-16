#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/create-filter.html
if __name__ == '__main__':
    """
	delete-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/delete-filter.html
	describe-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/describe-filter.html
	list-filters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/list-filters.html
    """

    parameter_display_string = """
    # name : The name of the filter to create.
    # dataset-group-arn : The ARN of the dataset group that the filter will belong to.
    # filter-expression : The filter expression that designates the interaction types that the filter will filter out. A filter expression must follow the following format:

EXCLUDE itemId WHERE INTERACTIONS.event_type in ("EVENT_TYPE")

Where âEVENT_TYPEâ is the type of event to filter out. To filter out all items with any interactions history, set "*" as the EVENT_TYPE. For more information, see Using Filters with Amazon Personalize .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("personalize", "create-filter", "name", "dataset-group-arn", "filter-expression", add_option_dict)
