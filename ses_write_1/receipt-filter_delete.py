#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/delete-receipt-filter.html
if __name__ == '__main__':
    """
	create-receipt-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/create-receipt-filter.html
	list-receipt-filters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/list-receipt-filters.html
    """

    parameter_display_string = """
    # filter-name : The name of the IP address filter to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ses", "delete-receipt-filter", "filter-name", add_option_dict)





