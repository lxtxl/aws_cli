#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-filter.html
if __name__ == '__main__':
    """
	create-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-filter.html
	delete-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-filter.html
	get-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-filter.html
	list-filters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-filters.html
    """

    parameter_display_string = """
    # detector-id : The unique ID of the detector that specifies the GuardDuty service where you want to update a filter.
    # filter-name : The name of the filter.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("guardduty", "update-filter", "detector-id", "filter-name", add_option_dict)
