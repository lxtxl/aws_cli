#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/update-revision.html
if __name__ == '__main__':
    """
	create-revision : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/create-revision.html
	delete-revision : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/delete-revision.html
	get-revision : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/get-revision.html
    """

    parameter_display_string = """
    # data-set-id : The unique identifier for a data set.
    # revision-id : The unique identifier for a revision.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("dataexchange", "update-revision", "data-set-id", "revision-id", add_option_dict)
