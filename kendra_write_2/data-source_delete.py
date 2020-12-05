#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/delete-data-source.html
if __name__ == '__main__':
    """
	create-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/create-data-source.html
	describe-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/describe-data-source.html
	list-data-sources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/list-data-sources.html
	update-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/update-data-source.html
    """

    parameter_display_string = """
    # id : The unique identifier of the data source to delete.
    # index-id : The unique identifier of the index associated with the data source.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kendra", "delete-data-source", "id", "index-id", add_option_dict)
