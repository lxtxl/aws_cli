#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/delete-filter.html
if __name__ == '__main__':
    """
	create-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/create-filter.html
	describe-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/describe-filter.html
	list-filters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/list-filters.html
    """

    parameter_display_string = """
    # filter-arn : The ARN of the filter to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("personalize", "delete-filter", "filter-arn", add_option_dict)





