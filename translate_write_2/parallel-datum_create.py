#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/create-parallel-data.html
if __name__ == '__main__':
    """
	delete-parallel-data : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/delete-parallel-data.html
	get-parallel-data : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/get-parallel-data.html
	list-parallel-data : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/list-parallel-data.html
	update-parallel-data : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/update-parallel-data.html
    """

    parameter_display_string = """
    # name : A custom name for the parallel data resource in Amazon Translate. You must assign a name that is unique in the account and region.
    # parallel-data-config : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("translate", "create-parallel-data", "name", "parallel-data-config", add_option_dict)
