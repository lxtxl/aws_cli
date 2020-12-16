#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-filter.html
if __name__ == '__main__':
    """
	delete-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-filter.html
	get-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-filter.html
	list-filters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-filters.html
	update-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-filter.html
    """

    parameter_display_string = """
    # detector-id : The unique ID of the detector of the GuardDuty account that you want to create a filter for.
    # name : The name of the filter.
    # finding-criteria : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("guardduty", "create-filter", "detector-id", "name", "finding-criteria", add_option_dict)
