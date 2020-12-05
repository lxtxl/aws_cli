#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-filter.html
if __name__ == '__main__':
    """
	create-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-filter.html
	delete-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-filter.html
	list-filters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-filters.html
	update-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-filter.html
    """

    parameter_display_string = """
    # detector-id : The unique ID of the detector that the filter is associated with.
    # filter-name : The name of the filter you want to get.
    """

    execute_two_parameter("guardduty", "get-filter", "detector-id", "filter-name", parameter_display_string)