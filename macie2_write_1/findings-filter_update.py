#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/update-findings-filter.html
if __name__ == '__main__':
    """
	create-findings-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/create-findings-filter.html
	delete-findings-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/delete-findings-filter.html
	get-findings-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/get-findings-filter.html
	list-findings-filters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/list-findings-filters.html
    """

    parameter_display_string = """
    # id : The unique identifier for the Amazon Macie resource or account that the request applies to.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("macie2", "update-findings-filter", "id", add_option_dict)





